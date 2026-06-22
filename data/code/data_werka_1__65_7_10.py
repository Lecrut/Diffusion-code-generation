class DynamicList:

    def __init__(self, data):
        self._data = data

    def get_element_by_position(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None
if __name__ == '__main__':
    SAMPLE_DATA = [5, 15, 25, 35, 45]
    my_list = DynamicList(SAMPLE_DATA)
    print(my_list.get_element_by_position(0))
    print(my_list.get_element_by_position(2))
    print(my_list.get_element_by_position(4))
    print(my_list.get_element_by_position(5))