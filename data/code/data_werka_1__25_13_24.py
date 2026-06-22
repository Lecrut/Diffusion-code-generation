def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [0, 1, -0.0, 0.0, None, '0', False]
    for val in test_values:
        print(is_zero(val))