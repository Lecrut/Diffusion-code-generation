class MiddleAccessor:
    _MIDDLE_OFFSET = 0

    def __init__(self, data):
        self._data = list(data)
        self._size = len(self._data)
        self._mid = self._size // 2

    def get_middle(self):
        if self._size == 0:
            raise ValueError("Empty list")
        return self._data[self._mid]

    def add(self, val):
        self._data.append(val)
        self._size += 1
        self._mid = self._size // 2

if __name__ == '__main__':
    container = MiddleAccessor([1, 2, 3, 4, 5])
    print(container.get_middle())
    container.add(6)
    print(container.get_middle())