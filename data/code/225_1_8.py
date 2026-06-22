def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    def is_valid(x):
        return isinstance(x, (int, float))
    
    filtered_data = [x for x in data if is_valid(x)]
    
    if not filtered_data:
        raise ValueError("No valid numeric values found in input list")
    
    minimum = filtered_data[0]
    maximum = filtered_data[0]
    for x in filtered_data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return (minimum, maximum)

if __name__ == '__main__':
    sample_list = [3, 1, "a", 4, 1, 5, 9, 2, 6]
    result = find_min_max(sample_list)
    print(result)