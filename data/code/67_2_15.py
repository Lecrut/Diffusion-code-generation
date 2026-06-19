def add_floats(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b

if __name__ == '__main__':
    try:
        result = add_floats(1.23456, 7.89012)
        print(result)
    except Exception as e:
        print(e)