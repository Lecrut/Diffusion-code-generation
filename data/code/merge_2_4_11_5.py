import sys
def process_choice(choice: int) -> None:
    if choice == 1:
        print("Action A executed.")
    elif choice == 2:
        print("Action B executed.")
    elif choice == 3:
        print("Action C executed.")
    else:
        raise ValueError(f"Invalid choice {choice}. Expected 1, 2, or 3.")
def main() -> None:
    sample_choices = [1, 2, 3]
    for i in range(len(sample_choices)):
        process_choice(choice=sample_choices[i])
if __name__ == '__main__':
    main()