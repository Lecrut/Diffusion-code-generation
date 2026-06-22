def find_largest_smallest_difference(nested_list):
    if not all(isinstance(sublist, list) and all(isinstance(item, int) for item in sublist) for sublist in nested_list):
        raise ValueError("Invalid input: Nested list must contain only integers.")
    
    flattened_list = [item for sublist in nested_list for item in sublist]
    if len(flattened_list) < 2:
        raise ValueError("Invalid input: Nested list must contain at least two elements.")
    
    return max(flattened_list) - min(flattened_list)

if __name__ == '__main__':
    sample_nested_list = [[3, 5, 1], [8, 2], [7]]
    try:
        result = find_largest_smallest_difference(sample_nested_list)
        print(result)
    except ValueError as e:
        print(e)