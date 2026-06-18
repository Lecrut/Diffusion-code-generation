import sys
def handle_selection(choice: str) -> None:
    if choice == "1":
        print("Option 1 executed successfully.")
    elif choice == "2":
        result = calculate_value(4, 5)
        print(f"Calculated value for Option 2 is {result}.")
    else:
        raise ValueError("Invalid option selected. Please choose between '1' and '2'.")
def calculate_value(a: int, b: int) -> int:
    return a + b
if __name__ == '__main__':
    sample_choices = ["1", "2"]
    for choice in sample_choices:
        try:
            handle_selection(choice)
        except ValueError as e:
            print(f"Error occurred: {e}", file=sys.stderr)