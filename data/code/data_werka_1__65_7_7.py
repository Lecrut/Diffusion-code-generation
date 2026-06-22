class DynamicList:

    def __init__(self, initial_data):
        self._data = initial_data

    def get_element(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError('Index out of range')
if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45]
    dynamic_list = DynamicList(sample_values)
    try:
        print(dynamic_list.get_element(0))
        print(dynamic_list.get_element(2))
        print(dynamic_list.get_element(4))
        print(dynamic_list.get_element(5))
    except IndexError as e:
        print(f'Caught expected error: {e}')