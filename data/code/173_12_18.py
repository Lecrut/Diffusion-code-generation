import itertools

def group_tuples_by_first_element(tuples_list):
    sorted_data = sorted(tuples_list)
    grouped_data = {key: list(group) for key, group in itertools.groupby(sorted_data, key=lambda x: x[0])}
    return grouped_data

if __name__ == '__main__':
    sample_data = [(3, 'c'), (1, 'a'), (2, 'b'), (3, 'd'), (1, 'e')]
    grouped_data = group_tuples_by_first_element(sample_data)
    for key, group in grouped_data.items():
        print(f'{key}: {group}')