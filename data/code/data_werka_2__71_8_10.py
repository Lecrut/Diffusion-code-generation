class ListWithMiddle:
    def __init__(self, items):
        self._items = list(items)
        self._length = len(self._items)
        self._middle_index = self._length // 2
        self._middle_value = self._items[self._middle_index] if self._length > 0 else None

    def get_middle(self):
        return self._middle_value

    def append(self, item):
        self._items.append(item)
        self._length += 1
        self._middle_index = self._length // 2
        self._middle_value = self._items[self._middle_index]

    def prepend(self, item):
        self._items.insert(0, item)
        self._length += 1
        self._middle_index = self._length // 2
        self._middle_value = self._items[self._middle_index]

    def remove_middle(self):
        if self._length == 0:
            raise ValueError("List is empty")
        removed = self._items.pop(self._middle_index)
        self._length -= 1
        if self._length > 0:
            self._middle_index = self._length // 2
            self._middle_value = self._items[self._middle_index]
        else:
            self._middle_value = None
        return removed

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        return self._items[index]

    def __repr__(self):
        return f"ListWithMiddle({self._items})"

if __name__ == '__main__':
    my_list = ListWithMiddle([10, 20, 30, 40, 50])
    middle_element = my_list.get_middle()
    print(middle_element)