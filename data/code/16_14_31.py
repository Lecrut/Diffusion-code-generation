def is_positive(number):
    return isinstance(number, (int, float)) and number > 0

if __name__ == '__main__':
    test_values = [10, -5, 0.5, -3.2, 'string', None, 7]
    results = {value: is_positive(value) for value in test_values}
    print(results)