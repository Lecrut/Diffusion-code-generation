def find_min_max(values):
    if not values:
        return None, None
    min_val = max_val = values[0]
    for value in values:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3.141592653589793, 2.718281828459045, 1.4142135623730951, 0.5772156649015328]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")