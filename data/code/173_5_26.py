def group_by_first_element(nested_list):
    grouped_dict = {}
    for sublist in nested_list:
        key = sublist[0]
        if key not in grouped_dict:
            grouped_dict[key] = []
        grouped_dict[key].extend(sublist[1:])
    return grouped_dict

if __name__ == '__main__':
    sample_data = [[1, 'a', 'b'], [2, 'c'], [1, 'd'], [3, 'e', 'f', 'g']]
    result = group_by_first_element(sample_data)
    print(result)