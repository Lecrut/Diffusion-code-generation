def group_by_first_element(nested_list):
    grouped_dict = {}
    for sublist in nested_list:
        key = sublist[0]
        if key not in grouped_dict:
            grouped_dict[key] = []
        grouped_dict[key].append(sublist[1:])
    return grouped_dict

if __name__ == '__main__':
    sample_data = [[1, 'a'], [2, 'b'], [1, 'c'], [3, 'd'], [2, 'e']]
    result = group_by_first_element(sample_data)
    print(result)