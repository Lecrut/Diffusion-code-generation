class TupleSorter:
    @staticmethod
    def sort_by_second_element(tuples):
        return sorted(tuples, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_data = [
        (1, 3),
        (4, 1),
        (2, 5),
        (7, 2)
    ]
    sorted_data = TupleSorter.sort_by_second_element(sample_data)
    print(sorted_data)