def is_odd(number):
    """Returns True if number is odd, False otherwise."""
    return number % 2 != 0

if __name__ == '__main__':
    test_values = [1, -3, 0, 4, 5]
    for val in test_values:
        result = is_odd(val)
        print(f"is_odd({val}) = {result}")