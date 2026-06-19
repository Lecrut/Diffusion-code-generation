class ListAccessor:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        self.data = data

    def get_element(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample_list)
    
    try:
        element_at_2 = accessor.get_element(2)
        print(f"Element at index 2: {element_at_2}")
        
        element_out_of_bounds = accessor.get_element(5)
    except IndexError as e:
        print(f"Caught expected error for index 5: {e}")
    
    try:
        non_integer_index = accessor.get_element("two")
    except TypeError as e:
        print(f"Caught expected error for non-integer index: {e}")