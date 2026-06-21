class StableTupleSorter:
    def __init__(self, tuples_list):
        if not all(isinstance(t, tuple) and len(t) == 2 for t in tuples_list):
            raise ValueError("All elements must be tuples of length 2.")
        self.tuples_list = tuples_list

    def sort_by_second_element(self):
        return sorted(self.tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_tuples = [(7, 3), (2, 1), (9, 2), (4, 2), (5, 3)]
    sorter = StableTupleSorter(sample_tuples)
    sorted_tuples = sorter.sort_by_second_element()
    print(sorted_tuples)