def is_even(number):
    if not isinstance(number, int) or number < 0:
        raise TypeError("Input must be a non-negative integer.")
    return number % 2 == 0
if __name__ == '__main__':
    test_cases = [10, -5, "4", 3.7]
    for value in test_cases:
        try:
            result = is_even(value)
            print(f"{value} is even.")
        except TypeError as e:
            print(f"Error processing {value}: {e}")