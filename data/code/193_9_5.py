def validate_input(values):
    if not hasattr(values, '__iter__'):
        raise TypeError("Input is not iterable")
    for value in values:
        if not isinstance(value, (int, float)):
            raise ValueError(f"Non-numeric value encountered: {value}")

def sum_values(values):
    total = 0
    for value in values:
        total += value
    return total

if __name__ == '__main__':
    sample_values = [1, 2, 3.5, 4]
    validate_input(sample_values)
    result = sum_values(sample_values)
    print(result)