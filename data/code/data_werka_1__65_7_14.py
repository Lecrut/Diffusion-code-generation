class DynamicList:

    def __init__(self, data):
        self._data = data

    def validate_index(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self._data):
            raise IndexError(f'Index {index} is out of bounds.')

    def get_element_by_position(self, index):
        self.validate_index(index)
        return self._data[index]
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    dynamic_list = DynamicList(sample_list)
    print(dynamic_list.get_element_by_position(0))
    print(dynamic_list.get_element_by_position(2))
    print(dynamic_list.get_element_by_position(4))
    try:
        print(dynamic_list.get_element_by_position(5))
    except IndexError as e:
        print(f'Caught expected error: {e}')