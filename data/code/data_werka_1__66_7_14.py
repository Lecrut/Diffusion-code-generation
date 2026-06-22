class AscendingComparer:

    def __init__(self, data):
        self.data = data

    def is_ascending(self):
        return [self.data[i] < self.data[i + 1] for i in range(len(self.data) - 1)]
if __name__ == '__main__':
    test_data_1 = [1, 2, 3, 4]
    test_data_2 = [1, 2, 2, 3]
    test_data_3 = [5, 4, 3, 2]
    test_data_4 = [1, 3, 2, 4]
    comparer_1 = AscendingComparer(test_data_1)
    comparer_2 = AscendingComparer(test_data_2)
    comparer_3 = AscendingComparer(test_data_3)
    comparer_4 = AscendingComparer(test_data_4)
    print(comparer_1.is_ascending())
    print(comparer_2.is_ascending())
    print(comparer_3.is_ascending())
    print(comparer_4.is_ascending())