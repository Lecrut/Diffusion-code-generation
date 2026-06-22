def check_float(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    test_value = 3.14
    result = check_float(test_value)
    print(result)