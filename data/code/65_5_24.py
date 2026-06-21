class FastAccessList:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0

    def append(self, value):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[self._size] = value
        self._size += 1

    def get(self, index):
        if not (0 <= index < self._size):
            raise IndexError('Index out of bounds')
        return self._data[index]

    def _resize(self, capacity):
        new_data = [None] * capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

if __name__ == '__main__':
    fast_list = FastAccessList()
    fast_list.append(10)
    fast_list.append(20)
    fast_list.append(30)
    print(fast_list.get(1))