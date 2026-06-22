def sum_two_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be integers or floats.")
    return a + b

if __name__ == '__main__':
    try:
        result = sum_two_numbers(100, 200)
        print(result)
    except ValueError as e:
        print(e)