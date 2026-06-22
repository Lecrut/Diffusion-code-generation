class IndexComparator:
    def __init__(self, data):
        self.data = data

    def compare_indices(self, idx1, idx2):
        return self.data[idx1] > self.data[idx2]

if __name__ == '__main__':
    sample_data = [100, 20, 30, 40, 50, 5]
    comparator = IndexComparator(sample_data)
    print(comparator.compare_indices(0, 5))
    print(comparator.compare_indices(5, 0))