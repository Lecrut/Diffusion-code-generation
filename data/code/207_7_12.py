def flatten_and_find_max(nested_list):
    if not isinstance(nested_list, list) or not all(isinstance(x, (list, int)) for x in nested_list):
        raise ValueError("Input must be a flat list of integers")
    
    flattened = [item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])]
    return max(flattened)

if __name__ == '__main__':
    sample1 = [[3, 5], [2, 8], [1]]
    result1 = flatten_and_find_max(sample1)
    print(f"List: {sample1}, Max: {result1}")
    
    sample2 = [4, 6, [7, 9], 8]
    result2 = flatten_and_find_max(sample2)
    print(f"List: {sample2}, Max: {result2}")
    
    sample3 = [[-1, -5], [-3, -2]]
    result3 = flatten_and_find_max(sample3)
    print(f"List: {sample3}, Max: {result3}")