class SafeListAccessor:

    def __init__(self, data):
        self._data = list(data)

    def get(self, index):
        if not -len(self._data) <= index < len(self._data):
            raise IndexError('Index out of bounds')
        return self._data[index]
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    accessor = SafeListAccessor(sample_list)
    print(accessor.get(0))
    print(accessor.get(2))
    print(accessor.get(-1))
    try:
        print(accessor.get(5))
    except IndexError as e:
        print(e)
    try:
        print(accessor.get(-6))
    except IndexError as e:
        print(e)