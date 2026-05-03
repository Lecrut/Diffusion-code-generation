class IndexOutOfBoundsError(Exception):
    pass
class ListAccessor:
    def __init__(self, data):
        self._data = list(data)
    def get_element(self, index):
        if not (0 <= index < len(self._data)):
            raise IndexOutOfBoundsError(f"Index {index} is out of bounds for list of size {len(self._data)}")
        return self._data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        print(f"Accessing index 2: {accessor.get_element(2)}")
        print(f"Accessing index 0: {accessor.get_element(0)}")
        accessor.get_element(5)
    except IndexOutOfBoundsError as e:
        print(f"Caught exception: {e}")
    try:
        accessor.get_element(-1)
    except IndexOutOfBoundsError as e:
        print(f"Caught exception: {e}")