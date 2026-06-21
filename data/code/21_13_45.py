class TupleSorter:

    def __init__(self, tuples_list):
        self.tuples_list = tuples_list

    def sort_by_second_element(self):
        return sorted(self.tuples_list, key=lambda x: x[1])

    def get_sorted_tuples(self):
        return self.sort_by_second_element()
if __name__ == '__main__':
    sample_tuples = [(7, 3), (2, 1), (5, 4), (3, 2), (6, 2)]
    sorter = TupleSorter(sample_tuples)
    sorted_tuples = sorter.get_sorted_tuples()
    print('Sorted tuples by second element:')
    print(sorted_tuples)
    another_sample_tuples = [(9, 8), (1, 5), (4, 5), (2, 3)]
    another_sorter = TupleSorter(another_sample_tuples)
    another_sorted_tuples = another_sorter.get_sorted_tuples()
    print('\nAnother sorted tuples by second element:')
    print(another_sorted_tuples)