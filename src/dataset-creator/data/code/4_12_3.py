import sys
def handle_selection(choice: str) -> None:
    if choice == "1":
        print("Option 1 executed successfully.")
    elif choice == "2":
        result = calculate_value(10, 5)
        print(f"Calculated value is {result}.")
    else:
        raise ValueError("Invalid selection provided. Please choose between '1' and '2'.")
def calculate_value(a: int, b: int) -> float:
    return a + b
if __name__ == '__main__':
    sample_choices = ["1", "2"]
    for choice in sample_choices:
        try:
            handle_selection(choice)
        except ValueError as e:
            print(f"Error occurred during processing of {choice}: {e}", file=sys.stderr)