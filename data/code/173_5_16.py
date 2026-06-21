def group_by_first_element(nested_list):
    if not isinstance(nested_list, list):
        raise ValueError("Input must be a list")
    
    grouped = {}
    for sublist in nested_list:
        if not isinstance(sublist, list) or len(sublist) < 2:
            raise ValueError("Each sublist must have at least two elements")
        
        key = sublist[0]
        value = sublist[1:]
        
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(value)
    
    return grouped

if __name__ == '__main__':
    sample_data = [[1, 'a'], [2, 'b'], [1, 'c'], [3, 'd'], [2, 'e']]
    result = group_by_first_element(sample_data)
    print(result)