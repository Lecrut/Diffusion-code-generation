def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    sample_values = [10, -5, 3.14, -2.71, 0, 'hello', None]
    for val in sample_values:
        print(f"{val}: {is_positive(val)}")