def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    
    return smallest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_smallest(sample_list)
    print(result)