def find_min_max(values):
    min_value = float('inf')
    max_value = float('-inf')
    for value in values:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    return min_value, max_value

if __name__ == '__main__':
    sample_values = [3.141592653589793, 2.718281828459045, 1.4142135623730951, 0.5772156649015328]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")