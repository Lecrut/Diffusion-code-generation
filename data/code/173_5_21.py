def group_by_first_element(nested_list):
    if not isinstance(nested_list, list):
        raise ValueError("Input must be a list.")
    
    grouped_dict = {}
    for sublist in nested_list:
        if not isinstance(sublist, list) or len(sublist) < 1:
            raise ValueError("Each element of the input list must be a non-empty list.")
        
        key = sublist[0]
        value = sublist[1:]
        
        if key not in grouped_dict:
            grouped_dict[key] = []
        grouped_dict[key].append(value)
    
    return grouped_dict

if __name__ == '__main__':
    sample_data = [[1, 'a'], [2, 'b'], [1, 'c'], [3, 'd'], [2, 'e']]
    result = group_by_first_element(sample_data)
    print(result)