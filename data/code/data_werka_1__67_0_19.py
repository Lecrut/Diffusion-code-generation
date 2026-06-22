def sum_two_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be integers or floats.")
    return a + b

if __name__ == '__main__':
    try:
        first_number = 123
        second_number = 456
        result = sum_two_numbers(first_number, second_number)
        print(result)
    except ValueError as e:
        print(e)