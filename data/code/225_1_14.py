def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    min_val = max_val = data[0]
    
    for element in data[1:]:
        if element < min_val:
            min_val = element
        elif element > max_val:
            max_val = element
    
    return (min_val, max_val)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_min_max(sample_values)
    print(result)