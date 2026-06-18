import sys

def check_parity(number: int) -> None:
    """Prints a clear message indicating if the number is even or odd."""
    status = "even" if number % 2 == 0 else "odd"
    print(f"The entered number {number} is {status}.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, arguments, network access, or file dependencies are needed.
    test_values = [4, -3, 0]

    for value in test_values:
        try:
            check_parity(value)
        except Exception as e:
            print(f"An error occurred while processing the number {value}: {e}", file=sys.stderr)