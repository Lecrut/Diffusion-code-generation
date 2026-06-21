import itertools

def group_by_first_element(tuples_list):
    return list(itertools.groupby(tuples_list, key=lambda x: x[0]))

if __name__ == '__main__':
    sample_data = [(1, 'a'), (2, 'b'), (2, 'c'), (3, 'd'), (3, 'e'), (3, 'f')]
    grouped_data = group_by_first_element(sample_data)
    for key, group in grouped_data:
        print(f"{key}: {list(group)}")