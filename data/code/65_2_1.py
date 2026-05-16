class ListAccessor:
    def __init__(self, data):
        self._data = data
    def get_element(self, position):
        if 0 <= position < len(self._data):
            return self._data[position]
        raise IndexError("Position out of bounds")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        element1 = accessor.get_element(2)
        print(f"Element at position 2: {element1}")
        element0 = accessor.get_element(0)
        print(f"Element at position 0: {element0}")
        element4 = accessor.get_element(4)
        print(f"Element at position 4: {element4}")
        accessor.get_element(5)
    except IndexError as e:
        print(f"Error caught: {e}")