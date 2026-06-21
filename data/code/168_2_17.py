def group_by_second_element(tuples_list):
    if not isinstance(tuples_list, list) or not all((isinstance(item, tuple) and len(item) == 2 for item in tuples_list)):
        raise ValueError('Input must be a list of tuples where each tuple contains exactly two elements.')
    grouped_dict = {}
    for first, second in tuples_list:
        if second not in grouped_dict:
            grouped_dict[second] = []
        grouped_dict[second].append(first)
    return grouped_dict
if __name__ == '__main__':
    sample_data = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'b')]
    result = group_by_second_element(sample_data)
    print(result)