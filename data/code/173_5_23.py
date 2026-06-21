def group_by_first_element(nested_list):
    if not all(isinstance(sublist, list) and len(sublist) > 0 for sublist in nested_list):
        raise ValueError("All elements must be non-empty lists")
    
    grouped_dict = {}
    for sublist in nested_list:
        key = sublist[0]
        if key not in grouped_dict:
            grouped_dict[key] = []
        grouped_dict[key].extend(sublist[1:])
    
    return grouped_dict

if __name__ == '__main__':
    sample_data = [[1, 'a'], [2, 'b'], [1, 'c'], [3, 'd'], [2, 'e']]
    result = group_by_first_element(sample_data)
    print(result)