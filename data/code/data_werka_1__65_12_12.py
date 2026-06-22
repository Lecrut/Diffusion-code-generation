MIN_INDEX = -1

class SafeListAccessor:
    def __init__(self, data):
        self._data = list(data)
    
    def get(self, index):
        if MIN_INDEX <= index < len(self._data):
            return self._data[index]
        raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = SafeListAccessor(sample_list)
    print(f"Element at index 0: {accessor.get(0)}")
    print(f"Element at index 2: {accessor.get(2)}")
    print(f"Element at index -1: {accessor.get(-1)}")
    try:
        accessor.get(5)
    except IndexError as e:
        print(f"Error caught: {e}")
    try:
        accessor.get(-6)
    except IndexError as e:
        print(f"Error caught: {e}")