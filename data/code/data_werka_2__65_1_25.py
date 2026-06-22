class ListAccessor:
    DEFAULT_LIST = [10, 20, 30, 40, 50]

    def __init__(self, elements=None):
        if elements is None:
            self.elements = ListAccessor.DEFAULT_LIST
        else:
            self.elements = elements

    @staticmethod
    def validate_index(index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= len(ListAccessor.DEFAULT_LIST):
            raise IndexError("Index out of bounds")

    def get_element(self, position):
        ListAccessor.validate_index(position)
        return self.elements[position]

if __name__ == '__main__':
    accessor = ListAccessor()
    print(f"Original list: {ListAccessor.DEFAULT_LIST}")
    try:
        element1 = accessor.get_element(2)
        print(f"Element at index 2: {element1}")
    except (TypeError, IndexError) as e:
        print(e)