class BoundaryExtractor:
    def __init__(self, data):
        if not data:
            raise ValueError("Data sequence cannot be empty")
        self._data = data

    def get_first(self):
        return self._data[0]

    def get_last(self):
        return self._data[-1]

    def get_boundary_pair(self):
        return self.get_first(), self.get_last()

if __name__ == '__main__':
    sample_values = [42, 17, 99, 8, 55]
    extractor = BoundaryExtractor(sample_values)
    print(extractor.get_first())
    print(extractor.get_last())
    print(extractor.get_boundary_pair())