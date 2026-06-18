def check_negative(number: float) -> bool:
    """Check if a given number is negative."""
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [1, -5, 0.34, -0.99]

    for num in samples:
        is_negative = check_negative(num)
        print(f"Number {num} {'is negative' if is_negative else 'is not negative'}")