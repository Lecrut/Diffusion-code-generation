class ListWithMiddle:
    def __init__(self, items):
        self._items = list(items)
        self._size = len(self._items)
        self._middle_index = self._size // 2

    def get_middle(self):
        if self._size == 0:
            raise ValueError("List is empty")
        return self._items[self._middle_index]

    def append(self, item):
        self._items.append(item)
        self._size += 1
        if self._size % 2 == 0:
            self._middle_index += 1

    def prepend(self, item):
        self._items.insert(0, item)
        self._size += 1
        if self._size % 2 == 0:
            self._middle_index -= 1

    def remove_middle(self):
        if self._size == 0:
            raise ValueError("List is empty")
        removed = self._items.pop(self._middle_index)
        self._size -= 1
        return removed

if __name__ == '__main__':
    my_list = ListWithMiddle([10, 20, 30, 40, 50])
    middle_value = my_list.get_middle()
    print(middle_value)
    
    my_list.append(60)
    new_middle = my_list.get_middle()
    print(new_middle)
    
    my_list.prepend(5)
    another_middle = my_list.get_middle()
    print(another_middle)