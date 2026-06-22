def flatten_and_find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    flattened_data = []
    stack = [data]
    
    while stack:
        current_element = stack.pop()
        if isinstance(current_element, list):
            stack.extend(reversed(current_element))
        else:
            flattened_data.append(current_element)
    
    return min(flattened_data)

if __name__ == '__main__':
    nested_list1 = [[5], [2, 8], 1]
    nested_list2 = []
    nested_list3 = [-10, [0, 5]]
    
    try:
        result1 = flatten_and_find_minimum(nested_list1)
        print(f"Minimum of {nested_list1}: {result1}")
        
        result3 = flatten_and_find_minimum(nested_list3)
        print(f"Minimum of {nested_list3}: {result3}")
        
        flatten_and_find_minimum(nested_list2)
    except ValueError as e:
        print(f"Caught expected error for empty list: {e}")