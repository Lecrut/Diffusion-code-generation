def find_min_max_values(nested_list):
    if not nested_list:
        return None, None
    
    min_val = float('inf')
    max_val = float('-inf')
    
    for item in nested_list:
        if isinstance(item, list):
            local_min, local_max = find_min_max_values(item)
            if local_min is not None and local_min < min_val:
                min_val = local_min
            if local_max is not None and local_max > max_val:
                max_val = local_max
        else:
            if item < min_val:
                min_val = item
            if item > max_val:
                max_val = item
    
    return min_val, max_val

if __name__ == '__main__':
    sample_list = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]
    min_val, max_val = find_min_max_values(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")