class AscendingComparer:
    def __init__(self, data):
        self.data = data

    def compare_adjacent(self):
        return [x < y for x, y in zip(self.data, self.data[1:])]

if __name__ == '__main__':
    sample_data_1 = [1, 2, 3, 4]
    sample_data_2 = [5, 3, 6, 7]
    sample_data_3 = [10, 10, 10, 10]

    comparer_1 = AscendingComparer(sample_data_1)
    comparer_2 = AscendingComparer(sample_data_2)
    comparer_3 = AscendingComparer(sample_data_3)

    print("Sample Data 1:", comparer_1.compare_adjacent())
    print("Sample Data 2:", comparer_2.compare_adjacent())
    print("Sample Data 3:", comparer_3.compare_adjacent())