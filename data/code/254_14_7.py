def flatten_and_find_min(nested_list):
    if not nested_list:
        raise ValueError("Input list cannot be empty")
    
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_find_min(item))
        else:
            flat_list.append(item)
    
    return min(flat_list)

if __name__ == '__main__':
    nested_list1 = [[5, 2], [8, 1]]
    nested_list2 = []
    nested_list3 = [[-10, 0], [5]]

    try:
        result1 = flatten_and_find_min(nested_list1)
        print(f"Minimum of {nested_list1}: {result1}")
        result3 = flatten_and_find_min(nested_list3)
        print(f"Minimum of {nested_list3}: {result3}")
        flatten_and_find_min(nested_list2)
    except ValueError as e:
        print(f"Caught expected error for empty list: {e}")