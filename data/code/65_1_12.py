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
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    print(f'Original list: {sample_list}')
    try:
        element1 = accessor.get_element_by_position(2)
        print(f'Element at index 2: {element1}')
        element0 = accessor.get_element_by_position(0)
        print(f'Element at index 0: {element0}')
        element4 = accessor.get_element_by_position(4)
        print(f'Element at index 4: {element4}')
        try:
            element_out_of_bounds = accessor.get_element_by_position(5)
        except IndexError as e:
            print(f'Caught expected error for index 5: {e}')
        try:
            element_negative = accessor.get_element_by_position(-1)
        except IndexError as e:
            print(f'Caught expected error for negative index -1: {e}')
    except TypeError as e:
        print(f'Caught unexpected type error: {e}')