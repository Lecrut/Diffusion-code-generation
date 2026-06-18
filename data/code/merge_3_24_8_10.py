def check_negative(number: int) -> str:
    """Returns a descriptive string confirming if the number is negative."""
    return f"The entered value {number} {'is' if number < 0 else 'is not'} negative."

if __name__ == '__main__':
    # Hard-coded sample values to avoid user input, command-line args, or network access.
    samples = [10, -5, 42, 0]

    for num in samples:
        result = check_negative(num)
        print(result)