def group_by_second_element(tuples_list):
    groups = {}
    for key, value in tuples_list:
        if value not in groups:
            groups[value] = []
        groups[value].append(key)
    return groups

if __name__ == '__main__':
    sample_data = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'b')]
    grouped_data = group_by_second_element(sample_data)
    print(grouped_data)