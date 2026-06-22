class ListAccessor:
    MAX_INDEX = 0
    MIN_INDEX = -1
    
    def __init__(self, data):
        self._data = list(data)
        self.MAX_INDEX = len(self._data) - 1
        self.MIN_INDEX = -len(self._data)
    
    @staticmethod
    def _is_valid_index(index, max_index, min_index):
        return min_index <= index <= max_index
    
    def get(self, index):
        if ListAccessor._is_valid_index(index, self.MAX_INDEX, self.MIN_INDEX):
            return self._data[index]
        raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    
    print(f"Element at index 0: {accessor.get(0)}")
    print(f"Element at index 2: {accessor.get(2)}")
    print(f"Element at index 4: {accessor.get(4)}")
    
    try:
        print(f"Element at index 5: {accessor.get(5)}")
    except IndexError as e:
        print(e)
    
    try:
        print(f"Element at index -6: {accessor.get(-6)}")
    except IndexError as e:
        print(e)