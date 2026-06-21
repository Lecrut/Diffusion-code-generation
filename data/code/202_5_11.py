def flatten_and_find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    flattened = []
    def flatten(sub_data):
        for item in sub_data:
            if isinstance(item, list):
                flatten(item)
            else:
                flattened.append(item)
    
    flatten(data)
    
    largest = max(flattened)
    return largest

if __name__ == '__main__':
    sample_list = [12, 45, [67, 89], 34, [91, 5]]
    result = flatten_and_find_largest(sample_list)
    print(result)