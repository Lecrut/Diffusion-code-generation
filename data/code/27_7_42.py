def is_not_equal(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both values must be numeric (int or float).")
    return a != b

if __name__ == '__main__':
    value1 = 27
    value2 = 3.14159
    result = is_not_equal(value1, value2)
    print(result)