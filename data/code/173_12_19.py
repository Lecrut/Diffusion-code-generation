from itertools import groupby

def sort_and_group_by_first_element(tuples_list):
    return [list(group) for _, group in groupby(sorted(tuples_list), key=lambda x: x[0])]

if __name__ == '__main__':
    sample_values = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
    print(sort_and_group_by_first_element(sample_values))