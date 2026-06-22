def is_positive_float(value):
    return value > 0.0

if __name__ == '__main__':
    test_values = [3.14, -2.71, 0.0, 1e-10, -1e-10]
    for val in test_values:
        print(is_positive_float(val))