import sys
def process_choice(choice: int) -> None:
    if choice == 1:
        print("Action One executed.")
    elif choice == 2:
        print("Action Two executed.")
    elif choice == 3:
        print("Action Three executed.")
    else:
        raise ValueError(f"Invalid choice {choice}.")
def main() -> None:
    choices = [1, 2, 3]
    for item in choices:
        try:
            process_choice(item)
        except (ValueError, IndexError):
            print("An error occurred.")
if __name__ == '__main__':
    main()