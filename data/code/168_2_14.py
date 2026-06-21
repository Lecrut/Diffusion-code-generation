GROUPING_KEY = 1

def group_by_second_element(tuples_list):
    grouped_dict = {}
    for key_value_tuple in tuples_list:
        key = key_value_tuple[GROUPING_KEY]
        if key not in grouped_dict:
            grouped_dict[key] = []
        grouped_dict[key].append(key_value_tuple[0])
    return grouped_dict

if __name__ == '__main__':
    sample_data = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'b')]
    print(group_by_second_element(sample_data))