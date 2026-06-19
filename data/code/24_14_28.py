def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-1, 0, 1, -2.5, 3.14]
    for val in test_values:
        print(is_negative(val))