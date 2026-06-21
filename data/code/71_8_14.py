class ListWithMiddle:
    def __init__(self, data):
        self._data = list(data)
        self._length = len(self._data)
        self._mid_index = self._length // 2

    def get_middle(self):
        if self._length == 0:
            raise ValueError("List is empty")
        return self._data[self._mid_index]

    def append(self, item):
        self._data.append(item)
        self._length += 1
        self._mid_index = self._length // 2

    def pop(self):
        if self._length == 0:
            raise ValueError("List is empty")
        self._data.pop()
        self._length -= 1
        self._mid_index = self._length // 2

if __name__ == '__main__':
    my_list = ListWithMiddle([10, 20, 30, 40, 50])
    middle_value = my_list.get_middle()
    print(middle_value)