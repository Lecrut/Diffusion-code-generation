def check_negative(number: float) -> bool:
    """Check if a given number is negative."""
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_values = [1, -5.5, 0]

    for value in test_values:
        result = check_negative(value)
        print(f"Is {value} negative? {'Yes' if result else 'No'}")