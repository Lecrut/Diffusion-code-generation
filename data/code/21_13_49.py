class TupleSorter:

    def __init__(self, tuples_list):
        self.tuples_list = tuples_list

    def sort_by_second_element(self):
        return sorted(self.tuples_list, key=lambda x: (x[1], x[0]))
if __name__ == '__main__':
    sample_tuples = [(1, 3), (4, 1), (5, 2), (6, 2), (7, 3)]
    sorter = TupleSorter(sample_tuples)
    sorted_tuples = sorter.sort_by_second_element()
    print('Sorted tuples by second element:')
    print(sorted_tuples)
    another_sample = [(10, 5), (20, 3), (30, 9), (40, 3)]
    another_sorter = TupleSorter(another_sample)
    sorted_another = another_sorter.sort_by_second_element()
    print('\nSorted another set of tuples by second element:')
    print(sorted_another)