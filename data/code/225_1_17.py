def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    def initialize_bounds():
        return data[0], data[0]
    
    def update_bounds(min_val, max_val, x):
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
        return min_val, max_val
    
    minimum, maximum = initialize_bounds()
    for x in data[1:]:
        minimum, maximum = update_bounds(minimum, maximum, x)
    
    return (minimum, maximum)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_min_max(sample_list)
    print(result)