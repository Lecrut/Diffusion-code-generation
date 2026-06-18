def check_negative(value: int) -> str:
    """Check if a given integer is negative."""
    return f"The value {value} {'is' if value < 0 else 'is not'} negative."

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    test_values = [-5, 0, 10]

    for num in test_values:
        result = check_negative(num)
        print(result)