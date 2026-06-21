class TupleSorter:
    @staticmethod
    def sort_tuples(data):
        return sorted(data, key=lambda x: (x[1], x[0]))

if __name__ == '__main__':
    sample_list = [(2, 3), (4, 1), (1, 2), (3, 1)]
    sorted_result = TupleSorter.sort_tuples(sample_list)
    print(sorted_result)