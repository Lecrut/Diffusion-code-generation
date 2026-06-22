def validate_index(index, length):
    if not (0 <= index < length):
        raise IndexError("Position out of bounds")

class ListAccessor:
    def __init__(self, data):
        self._data = data

    def get_element(self, position):
        validate_index(position, len(self._data))
        return self._data[position]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    accessor = ListAccessor(sample_list)
    try:
        element3 = accessor.get_element(2)
        print(f"Element at position 2: {element3}")
        element0 = accessor.get_element(0)
        print(f"Element at position 0: {element0}")
        element4 = accessor.get_element(4)
        print(f"Element at position 4: {element4}")
        accessor.get_element(5)
    except IndexError as e:
        print(f"Caught expected error: {e}")