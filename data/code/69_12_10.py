class ListElementAccessor:

    def __init__(self, data_list):
        self.data_list = data_list

    def get_element_by_index(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if index >= len(self.data_list) or index < -len(self.data_list):
            raise IndexError('Index out of bounds')
        return self.data_list[index]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = ListElementAccessor(sample_data)
    try:
        print(accessor.get_element_by_index(2))
        print(accessor.get_element_by_index(-1))
        print(accessor.get_element_by_index(5))
    except (IndexError, TypeError) as e:
        print(f'Caught error: {e}')