class ListElementAccessor:
    def __init__(self, data):
        self.data = data

    def get_element_at(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    accessor = ListElementAccessor(sample_data)
    
    try:
        index_to_access = 2
        element = accessor.get_element_at(index_to_access)
        print(f"Element at index {index_to_access}: {element}")
        
        another_index = 4
        another_element = accessor.get_element_at(another_index)
        print(f"Element at index {another_index}: {another_element}")
        
        invalid_index = 10
        invalid_element = accessor.get_element_at(invalid_index)
        print(f"Element at index {invalid_index}: {invalid_element}")
    except IndexError as e:
        print(f"Error: {e}")