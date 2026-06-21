def group_data_by_first_element(nested_list):
    grouped_dict = {}
    for sublist in nested_list:
        if sublist[0] not in grouped_dict:
            grouped_dict[sublist[0]] = []
        grouped_dict[sublist[0]].append(sublist[1:])
    return grouped_dict

if __name__ == '__main__':
    sample_data = [[1, 'a'], [2, 'b'], [1, 'c'], [3, 'd'], [2, 'e']]
    result = group_data_by_first_element(sample_data)
    print(result)