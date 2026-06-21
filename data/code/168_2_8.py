def group_by_second_element(tuples_list):
    grouped_dict = {}
    for key, value in tuples_list:
        if value not in grouped_dict:
            grouped_dict[value] = []
        grouped_dict[value].append(key)
    return grouped_dict

if __name__ == '__main__':
    sample_data = [(10, 'apple'), (20, 'banana'), (30, 'apple'), (40, 'cherry'), (50, 'banana')]
    result = group_by_second_element(sample_data)
    print(result)