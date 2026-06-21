def is_negative(value):
    return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    test_values = [-10, 5, -3.14, 2.71, 'world', None]
    results = {value: is_negative(value) for value in test_values}
    print(results)