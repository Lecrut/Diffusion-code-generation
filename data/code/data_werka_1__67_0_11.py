def sum_two_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    return a + b

if __name__ == '__main__':
    try:
        result = sum_two_numbers(123, 456)
        print(result)
    except TypeError as e:
        print(e)