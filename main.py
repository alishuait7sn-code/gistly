import json
import os
from datetime import datetime

# Path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, "vocabularies.json")


# ANSI Colors for a pretty terminal
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def main():
    folder = os.path.dirname(BASE_DIR)
    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)

    while True:
        try:
            choice = selected_method_number()
            if choice == "1":
                read()
            elif choice == "2":
                write()
            elif choice == "3":
                print(f"\n{Colors.YELLOW}Goodbye! Keep learning! 🚀{Colors.ENDC}")
                break
            else:
                print(f"{Colors.FAIL}Invalid selection. Try again.{Colors.ENDC}")
        except KeyboardInterrupt:
            break


def selected_method_number():
    print(f"\n{Colors.HEADER}{Colors.BOLD}╔════════════════════════════════════╗")
    print(f"║       LEXICON BUILDER 📚           ║")
    print(f"╚════════════════════════════════════╝{Colors.ENDC}")
    print(f"{Colors.BLUE} 1. {Colors.ENDC} View Library")
    print(f"{Colors.BLUE} 2. {Colors.ENDC} Add New Discovery")
    print(f"{Colors.BLUE} 3. {Colors.ENDC} Exit")
    print(f"{Colors.HEADER}──────────────────────────────────────{Colors.ENDC}")
    return input(f"{Colors.BOLD}Selection > {Colors.ENDC}").strip()


def write():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []

    new_id = data[-1]["id"] + 1 if data else 1

    print(f"\n{Colors.YELLOW}✨ New Entry #{new_id}{Colors.ENDC}")

    # Prettier input prompts
    content = input(f" ➜ {Colors.BOLD}Term:{Colors.ENDC} ")
    meaning = input(f" ➜ {Colors.BOLD}Definition:{Colors.ENDC} ")
    word_type = input(f" ➜ {Colors.BOLD}Category (e.g. Noun):{Colors.ENDC} ")
    example = input(f" ➜ {Colors.BOLD}Usage Example:{Colors.ENDC} ")
    synonyms_raw = input(f" ➜ {Colors.BOLD}Synonyms (comma-separated):{Colors.ENDC} ")

    new_entry = {
        "id": new_id,
        "content": content,
        "meaning": meaning,
        "type": word_type,
        "synonyms": [w.strip() for w in synonyms_raw.split(",") if w.strip()],
        "example": example,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    data.append(new_entry)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"\n{Colors.GREEN}✔ Successfully archived '{content}'!{Colors.ENDC}")


def read():
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print(f"\n{Colors.FAIL}Your library is empty.{Colors.ENDC}")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"\n{Colors.HEADER}{'ID':<4} | {'TERM':<15} | {'DEFINITION'}{Colors.ENDC}")
    print(f"─" * 50)

    for entry in data:
        print(
            f"{Colors.BLUE}{entry['id']:<4}{Colors.ENDC} | "
            f"{Colors.BOLD}{entry['content']:<15}{Colors.ENDC} | "
            f"{entry['meaning']}"
        )

    input(f"\n{Colors.YELLOW}[ Press Enter to return to menu ]{Colors.ENDC}")


if __name__ == "__main__":
    main()
