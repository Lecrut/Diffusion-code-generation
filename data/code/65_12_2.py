class ListAccessor:
    def __init__(self, data):
        self._data = list(data)
    def get(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        raise IndexError("Index out of bounds")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    print(f"Accessing index 0: {accessor.get(0)}")
    print(f"Accessing index 2: {accessor.get(2)}")
    print(f"Accessing index 4: {accessor.get(4)}")
    try:
        accessor.get(5)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    try:
        accessor.get(-1)
    except IndexError as e:
        print(f"Caught expected error: {e}")