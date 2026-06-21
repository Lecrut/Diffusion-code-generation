def find_largest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    largest = data[0]
    for element in data:
        if element > largest:
            largest = element
    
    return largest

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.99]
    result = find_largest_element(sample_list)
    print(result)