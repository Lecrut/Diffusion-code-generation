class TupleSorter:

    def __init__(self, tuples_list):
        self.tuples_list = tuples_list

    def sort_by_second_element(self):
        return sorted(self.tuples_list, key=lambda x: x[1])
if __name__ == '__main__':
    sample_tuples = [(7, 3), (2, 1), (9, 2), (4, 2), (6, 3)]
    sorter = TupleSorter(sample_tuples)
    sorted_tuples = sorter.sort_by_second_element()
    print('Sorted tuples:', sorted_tuples)
    another_sample_tuples = [(11, 5), (8, 3), (12, 9), (10, 3)]
    another_sorter = TupleSorter(another_sample_tuples)
    another_sorted_tuples = another_sorter.sort_by_second_element()
    print('Another sorted tuples:', another_sorted_tuples)