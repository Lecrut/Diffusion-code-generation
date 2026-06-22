class SafeListAccessor:

    def __init__(self, data):
        self._data = data

    def get(self, index):
        if not (0 <= index < len(self._data) or -len(self._data) <= index < 0):
            raise IndexError('Index out of bounds')
        return self._data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = SafeListAccessor(sample_list)
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