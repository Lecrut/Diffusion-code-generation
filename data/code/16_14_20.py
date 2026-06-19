def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.14, -2.71, 'hello', None]
    results = {value: is_positive(value) for value in sample_values}
    print(results)