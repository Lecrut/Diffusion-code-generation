def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [0, 1, -1, 0.0, -0.0, 1e-10, -1e-10]
    results = {v: is_zero(v) for v in test_values}
    print(results)