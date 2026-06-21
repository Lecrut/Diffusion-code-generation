class ListAccessor:
    OUT_OF_BOUNDS_ERROR_MESSAGE = "Index out of bounds"
    
    def __init__(self, data):
        self.data = data
    
    @staticmethod
    def is_valid_index(index, length):
        return isinstance(index, int) and 0 <= index < length
    
    def get_element(self, index):
        if not ListAccessor.is_valid_index(index, len(self.data)):
            raise ValueError(ListAccessor.OUT_OF_BOUNDS_ERROR_MESSAGE)
        return self.data[index]

if __name__ == '__main__':
    sample_list = [7, 17, 27, 37, 47]
    index_to_retrieve = 2
    accessor = ListAccessor(sample_list)
    try:
        element = accessor.get_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)