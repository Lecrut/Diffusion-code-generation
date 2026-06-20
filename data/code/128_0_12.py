def is_negative(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a numeric value")
    return number < 0

if __name__ == '__main__':
    test_numbers = [-10, 5, -3.14, 0]
    for num in test_numbers:
        try:
            result = is_negative(num)
            print(f"Testing number: {num}, Is negative: {result}")
        except ValueError as e:
            print(e)