def is_negative(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Unsupported type for input")
    return value < 0

if __name__ == '__main__':
    sample_values = [-1, 2, -3.5, 4.7, 0, 'test', None]
    results = {value: is_negative(value) if isinstance(value, (int, float)) else False for value in sample_values}
    print(results)