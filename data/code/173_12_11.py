import itertools

def group_tuples(tuples_list):
    return list(itertools.groupby(sorted(tuples_list), key=lambda x: x[0]))

if __name__ == '__main__':
    sample_values = [(3, 'c'), (1, 'a'), (2, 'b'), (1, 'd'), (3, 'e')]
    grouped_tuples = group_tuples(sample_values)
    print(grouped_tuples)