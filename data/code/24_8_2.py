def check_negative(value: int) -> str:
    """Returns a descriptive string indicating if the value is negative."""
    return f"The entered integer {value} {'is' if value < 0 else 'is not'} negative."

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    test_values = [-5, 10, -3]

    for num in test_values:
        result_message = check_negative(num)
        print(result_message)