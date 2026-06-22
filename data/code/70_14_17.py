class BoundaryAccessor:
    def __init__(self, data):
        if not hasattr(data, '__len__'):
            raise TypeError("Input must be a sequence")
        if len(data) == 0:
            raise ValueError("Sequence cannot be empty")
        self._first = data[0]
        self._last = data[-1]

    def get_first(self):
        return self._first

    def get_last(self):
        return self._last

    def get_bounds(self):
        return self._first, self._last

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    accessor = BoundaryAccessor(sample_data)
    result = accessor.get_bounds()
    print(result)