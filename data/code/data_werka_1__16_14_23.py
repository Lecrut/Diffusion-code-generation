def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    sample_values = [42, -7, 0, 3.14, -0.001, 'hello', None]
    for val in sample_values:
        print(f"{val}: {is_positive(val)}")