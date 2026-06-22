def is_negative(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Unsupported input type")
    return value < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.14, 2.71, 'hello', None]
    results = {value: is_negative(value) for value in sample_values if isinstance(value, (int, float))}
    print(results)