def is_even(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return (number & 1) == 0

if __name__ == '__main__':
    test_values = [2, 3, 0, -4, -5, 15, 16, -9, 8, 7]
    for value in test_values:
        try:
            result = is_even(value)
            print(f"{value} is even: {result}")
        except ValueError as e:
            print(f"Error checking {value}: {e}")