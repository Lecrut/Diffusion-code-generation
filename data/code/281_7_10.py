def calculate_sum(**kwargs):
    total = 0.0
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            total += value
    return total

if __name__ == '__main__':
    sample_values = {'a': 10, 'b': 20, 'c': 30, 'd': -5}
    result = calculate_sum(**sample_values)
    print(result)