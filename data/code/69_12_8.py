class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def _is_valid_index(self, index):
        return -len(self.data_list) <= index < len(self.data_list)

    def get_element(self, index):
        if not self._is_valid_index(index):
            raise IndexError("Index out of bounds")
        return self.data_list[index]

if __name__ == '__main__':
    my_list = [5, 15, 25, 35, 45]
    accessor = ListAccessor(my_list)
    
    try:
        print(f"Element at index 0: {accessor.get_element(0)}")
        print(f"Element at index -1: {accessor.get_element(-1)}")
        print(f"Element at index 2: {accessor.get_element(2)}")
        print(f"Element at index 4: {accessor.get_element(4)}")
        accessor.get_element(5)
    except IndexError as e:
        print(f"Caught expected error: {e}")