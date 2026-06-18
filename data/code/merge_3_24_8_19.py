def check_number(n: int) -> None:
    """Prints a descriptive statement confirming if the number is negative."""
    print(f"The entered value {n} {'is' if n < 0 else 'is not'} negative.")

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    test_values = [-5, -1, 0, 3]

    for value in test_values:
        check_number(value)