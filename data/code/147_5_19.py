class TupleSorter:
    def sort_tuples(self, data):
        if not data:
            return []
        try:
            sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
            return sorted_data
        except TypeError:
            return []

if __name__ == '__main__':
    sorter = TupleSorter()
    sample_list_1 = [(3, 2), (1, 1), (4, 1)]
    sample_list_2 = []
    sample_list_3 = [(5, 5), (3, 4), (6, 3), (7, 2), (8, 1)]
    print("Sample 1:", sorter.sort_tuples(sample_list_1))
    print("Sample 2:", sorter.sort_tuples(sample_list_2))
    print("Sample 3:", sorter.sort_tuples(sample_list_3))