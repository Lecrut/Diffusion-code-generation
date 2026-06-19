class SafeListAccessor:

    def __init__(self, data):
        self._data = list(data)

    def _is_valid_index(self, index):
        return -len(self._data) <= index < len(self._data)

    def get(self, index):
        if self._is_valid_index(index):
            return self._data[index]
        raise IndexError('Index out of bounds')
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date']
    accessor = SafeListAccessor(sample_data)
    print(accessor.get(0))
    print(accessor.get(-1))
    try:
        print(accessor.get(5))
    except IndexError as e:
        print(e)
    try:
        print(accessor.get(-6))
    except IndexError as e:
        print(e)