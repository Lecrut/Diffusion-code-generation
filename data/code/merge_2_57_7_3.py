class FastHTFAccessor:
    def __init__(self, data):
        if not isinstance(data, list) or len(data) == 0:
            raise TypeError("Input must be a non-empty numeric list")
        self._data = [float(x) for x in data]
    def _validate_index(self, idx):
        try:
            i = int(idx)
            if not (-len(self._data) <= i < len(self._data)):
                raise IndexError("Index out of bounds")
            return i
        except (ValueError, TypeError):
            raise TypeError(f"Invalid index type {type(idx).__name__}, expected numeric integer")
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            start = self._validate_index(idx.start) if idx.start is not None else 0
            stop = self._validate_index(idx.stop) if idx.stop is not None else len(self._data)
            step = int(idx.step) if idx.step is not None else 1
            return tuple(self._data[start:stop:step])
        i = self._validate_index(idx)
        return self._data[i]
if __name__ == '__main__':
    sample_data = [1.5, 2.7, -3.9, 4.0, 5.2]
    accessor = FastHTFAccessor(sample_data)
    print(accessor[0])
    print(accessor[-1])
    try:
        _ = accessor["a"]
    except TypeError as e:
        pass
    result_slice = accessor[slice(0, 3)]
    print(result_slice)