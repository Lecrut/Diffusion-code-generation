def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    def is_valid_number(item):
        return isinstance(item, (int, float))
    
    for item in data:
        if not is_valid_number(item):
            raise ValueError("All elements must be numbers")
    
    minimum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 9.99]
    result = find_minimum(sample_list)
    print(result)