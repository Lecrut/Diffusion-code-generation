import json
def process_choice(choice: str) -> None:
    if choice == "1":
        print("Action 1 executed.")
    elif choice == "2":
        print("Action 2 executed.")
    else:
        raise ValueError(f"Invalid choice: {choice}")
def main() -> None:
    input_choices = ["1", "invalid", "3"]
    for item in input_choices:
        try:
            process_choice(item)
        except ValueError as e:
            print(f"Error processing {item}: {e}")
if __name__ == '__main__':
    main()