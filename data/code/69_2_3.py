class IndexAccessor:
    def __init__(self, data):
        self._data = data
    def get(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = IndexAccessor(sample_list)
    print(f"Accessing index 0: {accessor.get(0)}")
    print(f"Accessing index 2: {accessor.get(2)}")
    print(f"Accessing index 4: {accessor.get(4)}")
    print(f"Accessing index 10 (out of bounds): {accessor.get(10)}")
    print(f"Accessing index -1 (out of bounds): {accessor.get(-1)}")