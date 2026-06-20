def is_even(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer.")
    return (number & 1) == 0

if __name__ == '__main__':
    test_numbers = [2, 3, 4, -6, -7]
    for num in test_numbers:
        try:
            print(f"Number {num} is even: {is_even(num)}")
        except ValueError as e:
            print(e)