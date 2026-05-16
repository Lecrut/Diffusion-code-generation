class IndexOutOfBoundsError(Exception):
    pass
class ListAccessor:
    def __init__(self, data):
        self._data = list(data)
    def get_element(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexOutOfBoundsError(f"Index {index} is out of bounds for list of size {len(self._data)}")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        element1 = accessor.get_element(2)
        print(f"Successfully retrieved element at index 2: {element1}")
        element_out_of_bounds = accessor.get_element(5)
    except IndexOutOfBoundsError as e:
        print(f"Caught expected exception: {e}")
    try:
        accessor.get_element(-1)
    except IndexOutOfBoundsError as e:
        print(f"Caught expected exception: {e}")