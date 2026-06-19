class DynamicList:
    def __init__(self, initial_data=None):
        self._data = initial_data if initial_data is not None else []

    def add_element(self, element):
        self._data.append(element)

    def get_element_by_position(self, position):
        return self._data[position]

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45]
    dynamic_list = DynamicList(sample_values)
    
    print(dynamic_list.get_element_by_position(0))
    print(dynamic_list.get_element_by_position(2))
    print(dynamic_list.get_element_by_position(4))
    
    try:
        print(dynamic_list.get_element_by_position(5))
    except IndexError as e:
        print(f"Caught expected error: {e}")