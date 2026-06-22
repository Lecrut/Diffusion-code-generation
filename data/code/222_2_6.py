def find_min_with_nan(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    min_value = None
    
    for value in data:
        if not isinstance(value, float):
            continue
        if min_value is None or value < min_value:
            min_value = value
    
    if min_value is None:
        raise ValueError("No valid floating-point numbers found")
    
    return min_value

if __name__ == '__main__':
    sample_list = [45.1, 12.3, float('nan'), 3.2, 56.7, 21.0]
    result = find_min_with_nan(sample_list)
    print(result)