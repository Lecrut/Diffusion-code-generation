class FastHFTAccessor:
    def __init__(self, data):
        if not isinstance(data, list) or (len(data) > 0 and not isinstance(data[0], (int, float))):
            raise TypeError("Input must be a list of numeric values.")
        self._data = tuple(data)
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise IndexError("Index must be an integer.")
        return self._data[index]
if __name__ == '__main__':
    sample_data = [1.5, 200.3, -456.789, 1e-5, 3.14159]
    accessor = FastHFTAccessor(sample_data)
    print(accessor[0])
    print(accessor[-1])