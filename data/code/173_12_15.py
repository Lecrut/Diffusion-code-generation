import itertools

class TupleGrouper:
    @staticmethod
    def group_by_first_element(tuples_list):
        return list(itertools.groupby(sorted(tuples_list), key=lambda x: x[0]))

if __name__ == '__main__':
    sample_data = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
    grouped_data = TupleGrouper.group_by_first_element(sample_data)
    for key, group in grouped_data:
        print(f'{key}: {list(group)}')