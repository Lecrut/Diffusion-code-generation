def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    current_min = data[0]
    for item in data[1:]:
        if item < current_min:
            current_min = item
    
    return current_min

if __name__ == '__main__':
    sample_list = [5, 12, 3, 8, 1, 15, -4, 9, 0, 22]
    minimum_value = find_minimum(sample_list)
    print("Minimum value:", minimum_value)