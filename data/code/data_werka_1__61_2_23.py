class ListAccessor:
    class OutOfBoundsError(Exception):
        def __init__(self, message):
            super().__init__(message)

    def __init__(self, elements):
        self.elements = elements

    def _validate_index(self, index):
        if not 0 <= index < len(self.elements):
            raise self.OutOfBoundsError(f'Index {index} is out of bounds for list of length {len(self.elements)}')

    def get_element(self, index):
        self._validate_index(index)
        return self.elements[index]

if __name__ == '__main__':
    sample_list = [7, 17, 27, 37, 47]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element(1))
        print(accessor.get_element(5))
    except ListAccessor.OutOfBoundsError as e:
        print(e)