class IndexComparator:
    def __init__(self, data):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input must be a list or tuple")
        if len(data) < 6:
            raise ValueError("List must have at least 6 elements")
        self._data = data

    def compare(self):
        return self._data[0] > self._data[5]

if __name__ == '__main__':
    sample_data = [99, 1, 2, 3, 4, 50]
    comparator = IndexComparator(sample_data)
    print(comparator.compare())