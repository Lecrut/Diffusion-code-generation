class BoundaryExtractor:
    def __init__(self, data):
        if not data:
            raise ValueError("Input sequence must contain at least one element")
        self._data = list(data)
        self._length = len(self._data)

    def get_boundary_indices(self):
        start_index = 0
        end_index = self._length - 1
        return start_index, end_index

    def get_values(self):
        start_idx, end_idx = self.get_boundary_indices()
        first_value = self._data[start_idx]
        last_value = self._data[end_idx]
        return first_value, last_value

if __name__ == '__main__':
    values = [7, 14, 21, 28, 35]
    extractor = BoundaryExtractor(values)
    result = extractor.get_values()
    print(result)