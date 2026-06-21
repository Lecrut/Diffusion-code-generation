class ElementAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        if not (-len(self.data_list) <= index < len(self.data_list)):
            raise IndexError("Index out of bounds")
        return self.data_list[index]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    accessor = ElementAccessor(my_list)
    
    try:
        element1 = accessor.get_element(2)
        print(f"Element at index 2: {element1}")
    except IndexError as e:
        print(f"Caught expected error: {e}")

    try:
        last_element = accessor.get_element(-1)
        print(f"Last element: {last_element}")
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")

    try:
        out_of_bounds_element = accessor.get_element(5)
    except IndexError as e:
        print(f"Caught expected error: {e}")