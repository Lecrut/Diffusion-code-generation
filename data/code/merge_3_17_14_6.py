import sys

def check_parity(number: int) -> None:
    """Prints a clear message indicating if the number is even or odd."""
    status = "even" if number % 2 == 0 else "odd"
    print(f"The number {number} is {status}.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input.
    test_cases = [1, 2, -3, 4]

    for value in test_cases:
        try:
            check_parity(value)
        except Exception as e:
            print(f"Error processing {value}: {e}", file=sys.stderr)