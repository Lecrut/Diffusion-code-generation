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
        element1 = accessor.get_element(2)
        print(f"Element at index 2: {element1}")
        
        last_element = accessor.get_element(-1)
        print(f"Last element: {last_element}")
        
        second_last_element = accessor.get_element(-2)
        print(f"Second last element: {second_last_element}")
        
        out_of_bounds_element = accessor.get_element(5)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    
    try:
        negative_out_of_bounds_element = accessor.get_element(-6)
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")