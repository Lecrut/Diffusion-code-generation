def validate_value(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number")
    if not (num > 0):
        return False
    if not (num % 2 == 0):
        return False
    if not (num < 100):
        return False
    return True

if __name__ == '__main__':
    test_input = 42
    result = validate_value(test_input)
    print(result)