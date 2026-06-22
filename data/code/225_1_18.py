def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    current_min = current_max = data[0]
    
    for value in data[1:]:
        if value < current_min:
            current_min = value
        elif value > current_max:
            current_max = value
    
    return (current_min, current_max)

if __name__ == '__main__':
    sample_list = [7, 3, 9, 2, 5, 1, 8]
    result = find_min_max(sample_list)
    print(result)