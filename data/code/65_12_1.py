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
    try:
        print(f"Element at index 0: {accessor.get(0)}")
        print(f"Element at index 2: {accessor.get(2)}")
        print(f"Element at index 4: {accessor.get(4)}")
        print(f"Element at index 5: {accessor.get(5)}")
    except IndexError as e:
        print(f"Error: {e}")