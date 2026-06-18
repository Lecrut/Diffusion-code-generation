def check_negative(value: int) -> str:
    """Returns a descriptive string indicating if the value is negative."""
    return f"The number {value} {'is' if value < 0 else 'is not'} negative."

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_values = [-5, 10, -3.5]

    for val in test_values:
        result = check_negative(int(val)) if isinstance(val, float) else check_negative(val)
        print(result)