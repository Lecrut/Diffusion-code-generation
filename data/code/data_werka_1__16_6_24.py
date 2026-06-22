def is_positive(value):
    return value > 0

if __name__ == '__main__':
    test_values = [1.5, -2.3, 0.0, 1e-308, -1e-308]
    results = {value: is_positive(value) for value in test_values}
    print(results)