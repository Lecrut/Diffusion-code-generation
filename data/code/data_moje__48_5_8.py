def find_largest_data_point(*collections):
    if not collections:
        raise ValueError("At least one collection must be provided")
    
    largest_value = None
    
    for collection in collections:
        for item in collection:
            if largest_value is None or item > largest_value:
                largest_value = item
                
    if largest_value is None:
        raise ValueError("No valid data points found in the provided collections")
        
    return largest_value

if __name__ == '__main__':
    list_a = [10, 25, 3, 45]
    list_b = [5, 12, 67, 8]
    list_c = [99, 4, 11, 30]
    
    result = find_largest_data_point(list_a, list_b, list_c)
    print(result)