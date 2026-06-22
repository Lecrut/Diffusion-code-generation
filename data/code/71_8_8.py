class ListWithMiddle:
    def __init__(self, elements):
        self._elements = list(elements)
        self._length = len(self._elements)
        self._middle_index = self._length // 2

    def get_middle(self):
        if self._length == 0:
            raise ValueError("List is empty")
        return self._elements[self._middle_index]

if __name__ == '__main__':
    my_list = ListWithMiddle([10, 20, 30, 40, 50])
    print(my_list.get_middle())