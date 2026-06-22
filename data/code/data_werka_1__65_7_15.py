class DynamicList:
    def __init__(self, data):
        self._data = data

    def get_element_by_position(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400, 500]
    my_dynamic_list = DynamicList(sample_values)
    
    positions_to_check = [0, 2, 4, 5]
    for position in positions_to_check:
        element = my_dynamic_list.get_element_by_position(position)
        if element is not None:
            print(f"Element at index {position}: {element}")
        else:
            print(f"No element found at index {position}")