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
    test_values = [10, 7, -3, 42]

    for value in test_values:
        check_parity(value)