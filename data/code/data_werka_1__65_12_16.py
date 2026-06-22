class SafeListAccessor:

    def __init__(self, data):
        self._data = list(data)

    def get(self, index):
        if -len(self._data) <= index < len(self._data):
            return self._data[index]
        raise IndexError('Index out of bounds')
if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    accessor = SafeListAccessor(SAMPLE_LIST)
    print(accessor.get(0))
    print(accessor.get(-1))
    try:
        print(accessor.get(5))
    except IndexError as e:
        print(f'Error: {e}')
    try:
        print(accessor.get(-6))
    except IndexError as e:
        print(f'Error: {e}')