class ListWithMiddle:
    def __init__(self, elements):
        self._elements = list(elements)
        self._length = len(self._elements)
        self._middle_index = self._length // 2
        self._middle_element = self._elements[self._middle_index] if self._length > 0 else None

    def get_middle(self):
        return self._middle_element

    def append(self, element):
        self._elements.append(element)
        self._length += 1
        new_middle_index = self._length // 2
        if new_middle_index != self._middle_index:
            self._middle_index = new_middle_index
            self._middle_element = self._elements[self._middle_index]

    def pop(self):
        if self._length == 0:
            raise ValueError("List is empty")
        self._elements.pop()
        self._length -= 1
        new_middle_index = self._length // 2
        if new_middle_index != self._middle_index:
            self._middle_index = new_middle_index
            self._middle_element = self._elements[self._middle_index] if self._length > 0 else None

if __name__ == '__main__':
    my_list = ListWithMiddle([1, 2, 3, 4, 5])
    middle = my_list.get_middle()
    print(middle)
    
    my_list.append(6)
    middle_after_append = my_list.get_middle()
    print(middle_after_append)
    
    my_list.pop()
    middle_after_pop = my_list.get_middle()
    print(middle_after_pop)