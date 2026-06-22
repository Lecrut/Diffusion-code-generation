class ListAccessor:
    OUT_OF_BOUNDS_MESSAGE = 'Index out of bounds'
    
    def __init__(self, elements):
        self.elements = elements
    
    @staticmethod
    def is_valid_index(index, length):
        return 0 <= index < length
    
    def get_element(self, index):
        if not self.is_valid_index(index, len(self.elements)):
            raise IndexError(self.OUT_OF_BOUNDS_MESSAGE)
        return self.elements[index]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element(2))
        print(accessor.get_element(6))
    except IndexError as e:
        print(e)