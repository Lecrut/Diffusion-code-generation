import sys

def check_parity(number: int) -> None:
    """Prints a clear message indicating if the number is even or odd."""
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

def validate_input(input_str: str) -> int | None:
    """Attempts to convert the input string to an integer. Returns None on failure."""
    try:
        return int(input_str.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or arguments
    test_cases = [0, 1, -2, "abc", "", 42]

    for value in test_cases:
        parsed_int = validate_input(str(value))
        
        if parsed_int is not None:
            check_parity(parsed_int)
        else:
            print(f"Error: Input '{value}' could not be converted to an integer.")