def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    test_values = [42, -7, 0, 3.14, -0.001, 'hello', None]
    results = {value: is_positive(value) for value in test_values}
    print(results)