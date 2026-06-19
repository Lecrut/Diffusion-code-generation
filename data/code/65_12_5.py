class SafeListAccessor:
    def __init__(self, data):
        self._data = list(data)

    def _validate_index(self, index):
        if not (-len(self._data) <= index < len(self._data)):
            raise IndexError("Index out of bounds")

    def get(self, index):
        self._validate_index(index)
        return self._data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = SafeListAccessor(sample_list)
    
    print(f"Element at index 0: {accessor.get(0)}")
    print(f"Element at index 2: {accessor.get(2)}")
    print(f"Element at index -1: {accessor.get(-1)}")
    
    try:
        print(f"Element at index 5: {accessor.get(5)}")
    except IndexError as e:
        print(e)
    
    try:
        print(f"Element at index -6: {accessor.get(-6)}")
    except IndexError as e:
        print(e)