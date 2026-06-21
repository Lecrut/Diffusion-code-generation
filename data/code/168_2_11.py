def group_by_second_element(tuples_list):
    grouped_dict = {}
    for key, value in tuples_list:
        if value not in grouped_dict:
            grouped_dict[value] = []
        grouped_dict[value].append(key)
    return grouped_dict

if __name__ == '__main__':
    sample_data = [(10, 'X'), (20, 'Y'), (30, 'X'), (40, 'Z'), (50, 'Y')]
    result = group_by_second_element(sample_data)
    print(result)