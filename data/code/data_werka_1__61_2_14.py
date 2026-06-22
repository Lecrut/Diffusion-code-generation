class ListAccessor:
    class OutOfBoundsError(Exception):
        def __init__(self, message):
            super().__init__(message)

    def __init__(self, elements):
        self.elements = elements

    def get_element(self, index):
        if 0 <= index < len(self.elements):
            return self.elements[index]
        else:
            raise ListAccessor.OutOfBoundsError(f'Index {index} is out of bounds for list of length {len(self.elements)}')

if __name__ == '__main__':
    sample_list = [7, 17, 27, 37, 47]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element(1))
        print(accessor.get_element(5))
    except ListAccessor.OutOfBoundsError as e:
        print(e)