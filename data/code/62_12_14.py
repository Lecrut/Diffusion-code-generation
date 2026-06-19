class ListAccessor:
    def __init__(self, data):
        self._data = list(data)
    
    def has_second_element(self):
        return len(self._data) > 1
    
    def get_second(self):
        if self.has_second_element():
            return self._data[1]
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    accessor = ListAccessor(sample_list)
    print(accessor.get_second())
    
    short_list = [5, 6]
    short_accessor = ListAccessor(short_list)
    print(short_accessor.get_second())
    
    single_element_list = [7]
    single_accessor = ListAccessor(single_element_list)
    print(single_accessor.get_second())