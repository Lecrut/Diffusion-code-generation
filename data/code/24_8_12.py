def check_number(n: int) -> None:
    """Prints a descriptive statement confirming if n is negative."""
    print(f"The number {n} {'is' if n < 0 else 'is not'} negative.")

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    test_values = [-5, 10, -3]

    for val in test_values:
        check_number(val)