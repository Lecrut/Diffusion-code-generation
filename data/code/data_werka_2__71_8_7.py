class MiddleList:
    def __init__(self, items):
        self._items = list(items)
        self._length = len(self._items)
        self._middle_index = self._length // 2

    def get_middle(self):
        if self._length == 0:
            raise ValueError("List is empty")
        return self._items[self._middle_index]

if __name__ == '__main__':
    my_list = MiddleList([10, 20, 30, 40, 50])
    result = my_list.get_middle()
    print(result)