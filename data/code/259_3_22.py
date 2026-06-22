def find_min_max(values):
    if not values:
        return None, None
    
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
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")