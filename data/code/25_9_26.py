def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [0, -0.0, 1e-20, 0.0000000001, 42, -3.14]
    results = {val: is_zero(val) for val in test_values}
    print(results)