class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    def get_element(self, position):
        if not isinstance(position, int):
            raise TypeError("Position must be an integer")
        if position < 0 or position >= len(self.elements):
            raise IndexError("Position out of range")
        return self.elements[position]

if __name__ == '__main__':
    SAMPLE_LIST = [100, 200, 300, 400, 500]
    accessor = ListAccessor(SAMPLE_LIST)
    try:
        element_at_index_2 = accessor.get_element(2)
        print(f"Element at index 2: {element_at_index_2}")
    except (IndexError, TypeError) as e:
        print(e)