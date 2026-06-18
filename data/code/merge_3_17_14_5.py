import sys

def is_even(n: int) -> bool:
    """Check if an integer n is even."""
    return n % 2 == 0

def validate_input(raw_value: str):
    """Attempt to parse a string into an integer. Raise ValueError on failure."""
    try:
        number = int(raw_value.strip())
        # Check for empty input after stripping whitespace
        if raw_value and not any(c.isdigit() or c in '+-' for c in raw_value):
            raise ValueError("Input must be a valid integer.")
        return number
    except ValueError as e:
        error_message = f"Invalid input '{raw_value}': {e}. Please provide an integer."
        sys.stderr.write(f"{error_message}\n")

if __name__ == '__main__':
    # Hard-coded sample values to run without user interaction
    test_inputs = ["42", "-7", "0"]

    for input_str in test_inputs:
        try:
            number = int(input_str)
            if is_even(number):
                message = f"The entered number {number} is EVEN."
            else:
                message = f"The entered number {number} is ODD."
            
            print(message)

        except ValueError as e:
            sys.stderr.write(f"Error processing input '{input_str}': {e}\n")