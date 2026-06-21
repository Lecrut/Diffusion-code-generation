class TupleSorter:
    @staticmethod
    def sort_by_second_element(tuples):
        return sorted(tuples, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 1), (5, 0)]
    sorted_tuples = TupleSorter.sort_by_second_element(sample_tuples)
    print(sorted_tuples)