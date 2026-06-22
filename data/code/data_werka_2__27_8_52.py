def check_difference(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be integers or floats.")
    return a != b

if __name__ == '__main__':
    try:
        value1 = 42.0
        value2 = 42
        result = check_difference(value1, value2)
        print(result)
    except ValueError as e:
        print(e)