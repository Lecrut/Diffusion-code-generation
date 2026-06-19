class ListAccessor:
    def __init__(self, data):
        self._internal_list = list(data)
    
    @classmethod
    def from_string(cls, data_str):
        return cls(data_str.split())
    
    def get_last_element(self):
        if not self._internal_list:
            return None
        return self._internal_list[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_data)
    last_element = accessor.get_last_element()
    print(last_element)
    
    sample_data_empty = []
    accessor_empty = ListAccessor(sample_data_empty)
    last_element_empty = accessor_empty.get_last_element()
    print(last_element_empty)
    
    sample_data_string = "apple banana cherry"
    accessor_from_string = ListAccessor.from_string(sample_data_string)
    last_element_string = accessor_from_string.get_last_element()
    print(last_element_string)