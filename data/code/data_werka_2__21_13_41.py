class TupleSorter:

    def __init__(self, tuples_list):
        self.tuples_list = tuples_list

    def sort_by_second_element(self):
        return sorted(self.tuples_list, key=lambda x: x[1])
if __name__ == '__main__':
    sample_tuples = [(7, 2), (3, 4), (9, 1), (5, 2), (8, 3)]
    sorter = TupleSorter(sample_tuples)
    sorted_tuples = sorter.sort_by_second_element()
    print('Sorted by second element:', sorted_tuples)
    another_sample = [(2, 5), (6, 1), (4, 5), (1, 3)]
    sorter.tuples_list = another_sample
    print('Another sorted list:', sorter.sort_by_second_element())