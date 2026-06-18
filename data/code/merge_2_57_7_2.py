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
            return True
        except (ValueError, TypeError):
            raise ValueError("Index must be an integer")
    def __getitem__(self, idx):
        self._validate_index(idx)
        if isinstance(idx, slice):
            start = int(idx.start) or 0
            stop = int(idx.stop) or len(self._data)
            step = int(idx.step) or 1
            return [self._data[i] for i in range(start, stop, step)]
        else:
            if isinstance(idx, bool):
                raise TypeError("Boolean index not allowed")
            self._validate_index(idx)
            return float(self._data[idx])
if __name__ == '__main__':
    sample_data = [1.5, 2.73e-4, -0.0089, 1.2]
    accessor = FastHTFAccessor(sample_data)
    print(accessor[0])
    print(accessor[-1])
    try:
        _ = accessor["a"]
    except ValueError as e:
        pass