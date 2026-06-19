class ListAccessor:
    OUT_OF_BOUNDS_MESSAGE = 'Index out of bounds'
    
    @staticmethod
    def validate_index(index, length):
        if not 0 <= index < length:
            raise IndexError(ListAccessor.OUT_OF_BOUNDS_MESSAGE)
    
    def __init__(self, elements):
        self.elements = elements
    
    def get_element(self, index):
        ListAccessor.validate_index(index, len(self.elements))
        return self.elements[index]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element(2))
        print(accessor.get_element(6))
    except IndexError as e:
        print(e)