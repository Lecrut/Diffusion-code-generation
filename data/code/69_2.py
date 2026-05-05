class IndexAccessor:
    def __init__(self, data):
        self._data = data
    def get_element(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = IndexAccessor(sample_list)
    print(f"Accessing index 0: {accessor.get_element(0)}")
    print(f"Accessing index 2: {accessor.get_element(2)}")
    print(f"Accessing index 4: {accessor.get_element(4)}")
    print(f"Accessing index 5 (out of bounds): {accessor.get_element(5)}")
    print(f"Accessing index -1 (out of bounds): {accessor.get_element(-1)}")