import sys

def check_parity(number: int) -> None:
    """Prints a clear message indicating if the number is even or odd."""
    if number % 2 == 0:
        print(f"The integer {number} is even.")
    else:
        print(f"The integer {number} is odd.")

def handle_non_integer_input() -> None:
    """Handles cases where input cannot be converted to an integer."""
    print("Error: Non-integer value received. Please ensure a valid integer is provided.", file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    try:
        # Simulating reading from standard input with hard-coded sample values as per constraints
        inputs = [42, 73, -8]

        for val in inputs:
            check_parity(val)
    except ValueError as e:
        handle_non_integer_input()