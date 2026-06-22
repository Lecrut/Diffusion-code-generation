class ListWithMiddle:
    def __init__(self, items):
        self._items = list(items)
        self._length = len(self._items)
        self._mid_index = self._length // 2
        if self._length % 2 == 0 and self._length > 0:
            self._mid_index -= 1

    def get_middle(self):
        if self._length == 0:
            raise ValueError("List is empty")
        return self._items[self._mid_index]

if __name__ == '__main__':
    my_list = ListWithMiddle([1, 2, 3, 4, 5])
    print(my_list.get_middle())
    
    my_list2 = ListWithMiddle([10, 20, 30, 40])
    print(my_list2.get_middle())