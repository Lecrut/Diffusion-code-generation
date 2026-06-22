def flatten_and_find_min(nested_list):
    if not nested_list:
        raise ValueError("Input list cannot be empty")
    
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_and_find_min(element))
        else:
            flat_list.append(element)
    
    return min(flat_list)

if __name__ == '__main__':
    sample_list1 = [5, 2, [8, 1]]
    sample_list2 = []
    sample_list3 = [-10, 0, [5, -5]]

    try:
        result1 = flatten_and_find_min(sample_list1)
        print(f"Minimum of {sample_list1}: {result1}")
        
        result3 = flatten_and_find_min(sample_list3)
        print(f"Minimum of {sample_list3}: {result3}")
        
        flatten_and_find_min(sample_list2)
    except ValueError as e:
        print(f"Caught expected error for empty list: {e}")