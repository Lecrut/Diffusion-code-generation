def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [0, 1, -0.0, 1e-308, '0', 2 + 2j]
    results = [is_zero(val) for val in test_values]
    print(results)