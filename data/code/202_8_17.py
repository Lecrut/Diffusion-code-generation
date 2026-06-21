def find_max_mixed(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    max_val = None
    for item in numbers:
        if max_val is None or (isinstance(item, int) and isinstance(max_val, int) and item > max_val) or \
           (isinstance(item, float) and isinstance(max_val, float) and item > max_val):
            max_val = item
    
    if max_val is None:
        raise ValueError("Input list must contain at least one numeric value")
    
    return max_val

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, '10', -1]
    try:
        print(find_max_mixed(sample_values))
    except ValueError as e:
        print(e)