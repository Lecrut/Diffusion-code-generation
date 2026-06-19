class ListAccessor:

    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError('Data must be a list')
        self.data = data

    def get_element(self, index):
        self._validate_index(index)
        return self.data[index]

    def _validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if index < 0 or index >= len(self.data):
            raise IndexError('Index out of bounds')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        element_at_2 = accessor.get_element(2)
        print(f'Element at index 2: {element_at_2}')
        element_at_0 = accessor.get_element(0)
        print(f'Element at index 0: {element_at_0}')
        element_at_4 = accessor.get_element(4)
        print(f'Element at index 4: {element_at_4}')
        element_out_of_bounds = accessor.get_element(5)
    except IndexError as e:
        print(f'Caught expected error for index 5: {e}')
    try:
        element_non_integer = accessor.get_element('two')
    except TypeError as e:
        print(f'Caught expected error for non-integer index: {e}')