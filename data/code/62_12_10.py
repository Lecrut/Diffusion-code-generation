class SafeListAccessor:
    def __init__(self, data):
        self._data = list(data)
    
    def _validate_index(self, index):
        return 0 <= index < len(self._data)
    
    def get_second(self):
        if self._validate_index(1):
            return self._data[1]
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    accessor = SafeListAccessor(sample_list)
    second_element = accessor.get_second()
    print(second_element)

    short_list = [5, 6]
    short_accessor = SafeListAccessor(short_list)
    second_short_element = short_accessor.get_second()
    print(second_short_element)

    single_element_list = [7]
    single_accessor = SafeListAccessor(single_element_list)
    second_single_element = single_accessor.get_second()
    print(second_single_element)