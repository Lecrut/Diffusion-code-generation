class ListAccessor:
    def __init__(self, data):
        self._data = data

    def get_first(self):
        if len(self._data) == 0:
            raise IndexError("list index out of range")
        return self._data[0]

    def get_count(self):
        return len(self._data)

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample_data)
    print(accessor.get_first())
    print(accessor.get_count())