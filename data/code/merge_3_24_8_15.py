def check_negative(value: int) -> str:
    """Returns a descriptive string indicating if an integer is negative."""
    if value < 0:
        return f"The number {value} is negative."
    else:
        return f"The number {value} is not negative (zero or positive)."

if __name__ == '__main__':
    # Sample values to test without user input
    sample_values = [-5, 0, 3]

    for num in sample_values:
        result = check_negative(num)
        print(result)