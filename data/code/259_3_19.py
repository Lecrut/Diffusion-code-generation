def find_min_max(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    
    min_val = float('inf')
    max_val = float('-inf')
    
    for value in values:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3.141592653589793, 2.718281828459045, 1.618033988749895, 0.5772156649015328]
    try:
        min_val, max_val = find_min_max(sample_values)
        print(f"Minimum: {min_val}, Maximum: {max_val}")
    except ValueError as e:
        print(e)