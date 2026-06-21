class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        if not (-len(self.data_list) <= index < len(self.data_list)):
            raise IndexError("Index out of bounds")
        return self.data_list[index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_data)
    
    try:
        element_at_positive_index = accessor.get_element(2)
        print(f"Element at index 2: {element_at_positive_index}")
    except IndexError as e:
        print(f"Caught expected error for positive index: {e}")

    try:
        element_at_negative_index = accessor.get_element(-1)
        print(f"Element at index -1: {element_at_negative_index}")
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")

    try:
        out_of_bounds_positive_index = accessor.get_element(5)
    except IndexError as e:
        print(f"Caught expected error for out-of-bounds positive index: {e}")

    try:
        out_of_bounds_negative_index = accessor.get_element(-6)
    except IndexError as e:
        print(f"Caught expected error for out-of-bounds negative index: {e}")