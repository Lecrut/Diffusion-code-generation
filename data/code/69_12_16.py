class ListAccessor:
    POSITIVE_INDEX_START = 0
    NEGATIVE_INDEX_START = -1

    @staticmethod
    def get_element(data_list, index):
        if not (ListAccessor.POSITIVE_INDEX_START <= index < len(data_list) or 
                ListAccessor.NEGATIVE_INDEX_START >= index > -(len(data_list))):
            raise IndexError("Index out of bounds")
        return data_list[index]

if __name__ == '__main__':
    accessor = ListAccessor()
    my_list = [10, 20, 30, 40, 50]
    try:
        element1 = accessor.get_element(my_list, 2)
        print(f"Element at index 2: {element1}")
        element_out_of_bounds = accessor.get_element(my_list, 5)
    except IndexError as e:
        print(f"Caught expected error for positive index: {e}")
    
    try:
        last_element = accessor.get_element(my_list, -1)
        print(f"Element at negative index -1: {last_element}")
        element_out_of_bounds_negative = accessor.get_element(my_list, -6)
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")