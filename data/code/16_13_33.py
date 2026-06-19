def is_positive(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an integer or a float")
    return number > 0

if __name__ == '__main__':
    sample_values = [10, -5, 0.0, 3.14, -2.718, 'string', None]
    results = {value: is_positive(value) for value in sample_values if isinstance(value, (int, float))}
    print(results)