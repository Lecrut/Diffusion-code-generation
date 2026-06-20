class ListElementAccessor:
    def get_element(self, data_list, index):
        if not isinstance(data_list, list) or not all(isinstance(item, (int, float)) for item in data_list):
            raise ValueError("Data must be a list of numbers")
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index >= len(data_list) or index < -len(data_list):
            raise IndexError("Index out of bounds")
        return data_list[index]

if __name__ == '__main__':
    accessor = ListElementAccessor()
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
        print(f"Caught expected error for negative index: {e}")
    try:
        accessor.get_element([10, '20', 30], 1)
    except ValueError as e:
        print(f"Caught expected error for non-numeric data: {e}")
    try:
        accessor.get_element(my_list, "2")
    except TypeError as e:
        print(f"Caught expected error for non-integer index: {e}")