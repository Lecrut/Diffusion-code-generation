def validate_float_value(var):
    try:
        if not isinstance(var, float):
            raise ValueError("Input is not a float")
        if var != 3.14:
            return False
        return True
    except ValueError as e:
        print(e)
        return False

if __name__ == '__main__':
    test_values = [3.14, 3.14159, '3.14', 3, 3.1400000000000001]
    for value in test_values:
        result = validate_float_value(value)
        print(result)