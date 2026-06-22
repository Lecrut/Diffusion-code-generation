class ListAccessor:

    class OutOfBoundsError(Exception):

        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    def __init__(self, elements):
        self.elements = elements

    def get_element(self, index):
        if 0 <= index < len(self.elements):
            return self.elements[index]
        else:
            raise self.OutOfBoundsError(f'Index {index} is out of bounds for list of length {len(self.elements)}')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element(2))
        print(accessor.get_element(5))
    except ListAccessor.OutOfBoundsError as e:
        print(e)