class ListAccessor:

    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError('Data must be a list')
        self.data = data

    def get_element_by_position(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if index < 0 or index >= len(self.data):
            raise IndexError('Index out of bounds')
        return self.data[index]
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    accessor = ListAccessor(sample_list)
    try:
        element_at_2 = accessor.get_element_by_position(2)
        print(f'Element at index 2: {element_at_2}')
        element_at_0 = accessor.get_element_by_position(0)
        print(f'Element at index 0: {element_at_0}')
        element_at_4 = accessor.get_element_by_position(4)
        print(f'Element at index 4: {element_at_4}')
        element_out_of_bounds = accessor.get_element_by_position(5)
    except IndexError as e:
        print(f'Caught expected error for index 5: {e}')
    try:
        element_non_integer = accessor.get_element_by_position('two')
    except TypeError as e:
        print(f'Caught expected error for non-integer index: {e}')