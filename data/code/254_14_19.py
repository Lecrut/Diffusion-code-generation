def flatten_and_find_minimum(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_find_minimum(item))
        else:
            flat_list.append(item)
    return min(flat_list)

if __name__ == '__main__':
    sample1 = [3, 5, [2, 8], -1]
    sample2 = [[-4, 0], [7, 1], 9]
    sample3 = []
    
    result1 = flatten_and_find_minimum(sample1)
    print(f"Minimum of {sample1}: {result1}")
    
    result2 = flatten_and_find_minimum(sample2)
    print(f"Minimum of {sample2}: {result2}")
    
    try:
        result3 = flatten_and_find_minimum(sample3)
    except ValueError as e:
        print(f"Caught expected error for empty list: {e}")