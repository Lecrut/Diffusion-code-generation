class SafeListAccessor:
    def __init__(self, data):
        self._data = data
    def get_element_safe(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = SafeListAccessor(sample_list)
    print(accessor.get_element_safe(2))
    print(accessor.get_element_safe(0))
    print(accessor.get_element_safe(5))
    print(accessor.get_element_safe(-1))