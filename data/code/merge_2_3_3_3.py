def is_even(number):
    if not isinstance(number, int):
        raise TypeError(f"Expected an integer, got {type(number).__name__}")
    return number % 2 == 0
if __name__ == '__main__':
    test_cases = [42, -17, 3.5, "five", True]
    for value in test_cases:
        try:
            result = is_even(value)
            print(f"{value} is even: {result}")
        except TypeError as e:
            print(f"Error processing {type(value).__name__}: {e}")