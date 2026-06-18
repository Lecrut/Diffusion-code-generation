def check_parity(number: int) -> None:
    """Prints a clear message indicating if the number is even or odd."""
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

def handle_input_error(input_str: str) -> None:
    """Handles cases where the input cannot be converted to an integer."""
    try:
        int_value = int(input_str.strip())
        check_parity(int_value)
    except ValueError:
        print(f"Error: '{input_str}' is not a valid integer.")

if __name__ == '__main__':
    # Sample values run without user input, command-line arguments, or network access.
    test_cases = ["4", "7", "-3", "+10"]

    for case in test_cases:
        handle_input_error(case)

        print("---")  # Separator between tests