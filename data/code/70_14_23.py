class BoundaryAccessor:
    _EMPTY_LIST_ERROR = "List must not be empty"

    def __init__(self, data):
        self._data = data

    def get_first_and_last(self):
        if len(self._data) == 0:
            raise ValueError(self._EMPTY_LIST_ERROR)
        return self._data[0], self._data[-1]

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28, 35]
    accessor = BoundaryAccessor(sample_data)
    result = accessor.get_first_and_last()
    print(result)