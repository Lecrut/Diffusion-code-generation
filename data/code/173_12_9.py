from itertools import groupby

def sort_and_group_tuples(tuples_list):
    return [(key, list(group)) for key, group in groupby(sorted(tuples_list), key=lambda x: x[0])]

if __name__ == '__main__':
    sample_data = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
    print(sort_and_group_tuples(sample_data))