def find_min_max(values):
    if not isinstance(values, list) or not all(isinstance(x, (int, float)) for x in values):
        raise ValueError("Input must be a list of numbers")
    
    min_val = max_val = values[0]
    for value in values[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4, 8, 6, 7]
    print(find_min_max(sample_values))