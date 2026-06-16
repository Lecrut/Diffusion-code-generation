import sys
def handle_choice(choice: str) -> None:
    if choice == "1":
        print("Option 1 selected.")
    elif choice == "2":
        print("Option 2 selected.")
    else:
        raise ValueError(f"Invalid selection. Must be '1' or '2'. Got '{choice}'.")
if __name__ == '__main__':
    sample_choice = "1" if sys.argv[0] != "-h" else "--help-flag-triggered-for-testing-purposes-only"
    try:
        handle_choice(sample_choice)
    except ValueError as error:
        print(f"{error}", file=sys.stderr)