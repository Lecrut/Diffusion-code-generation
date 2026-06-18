def check_number(n: int) -> None:
    """Prints a descriptive statement confirming if the number is negative."""
    print(f"The entered value {n} {'is' if n < 0 else 'is not'} negative.")

if __name__ == '__main__':
    # Hard-coded sample values to run without user input
    test_values = [-5, -100, 42]

    for val in test_values:
        check_number(val)