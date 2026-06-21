class BoundaryExtractor:
    def __init__(self, source_list):
        self._data = list(source_list)

    def extract(self):
        if len(self._data) == 0:
            raise ValueError("List must not be empty")
        return (self._data[0], self._data[-1])

    def count(self):
        return len(self._data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    extractor = BoundaryExtractor(sample_data)
    first, last = extractor.extract()
    print(first)
    print(last)
    print(extractor.count())