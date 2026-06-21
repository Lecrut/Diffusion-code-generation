class TupleSorter:
    def __init__(self, tuples_list):
        self.tuples_list = tuples_list

    def sort_by_second_element(self):
        return sorted(self.tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_tuples = [(10, 5), (20, 3), (30, 9), (40, 3)]
    sorter = TupleSorter(sample_tuples)
    sorted_tuples = sorter.sort_by_second_element()
    print(sorted_tuples)