def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [0, 0.0, -0, -0.0, 1, 1.0]
    results = {value: is_zero(value) for value in test_values}
    print(results)