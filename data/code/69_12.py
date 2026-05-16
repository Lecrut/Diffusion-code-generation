class IndexAccessor:
    def get_element(self, data_list, index):
        if not (0 <= index < len(data_list)):
            raise IndexError("Index out of bounds")
        return data_list[index]
if __name__ == '__main__':
    accessor = IndexAccessor()
    my_list = [10, 20, 30, 40, 50]
    try:
        element1 = accessor.get_element(my_list, 2)
        print(f"Element at index 2: {element1}")
        element_out_of_bounds = accessor.get_element(my_list, 5)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    try:
        accessor.get_element(my_list, -1)
    except IndexError as e:
        print(f"Caught expected error: {e}")