def validate_input(tuples_list):
    if not isinstance(tuples_list, list):
        raise ValueError("Input must be a list")
    for item in tuples_list:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("List elements must be tuples of length 2")

def group_by_second_element(tuples_list):
    validate_input(tuples_list)
    grouped_dict = {}
    for key, value in tuples_list:
        if value not in grouped_dict:
            grouped_dict[value] = []
        grouped_dict[value].append(key)
    return grouped_dict

if __name__ == '__main__':
    sample_data = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'b')]
    print(group_by_second_element(sample_data))