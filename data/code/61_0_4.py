def get_element_safely(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return None

class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def access(self, index):
        return get_element_safely(self.data_list, index)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_data)
    
    valid_index = 2
    invalid_index = 7
    
    element_valid = accessor.access(valid_index)
    element_invalid = accessor.access(invalid_index)
    
    print(f"List: {sample_data}")
    print(f"Element at index {valid_index}: {element_valid}")
    print(f"Element at index {invalid_index}: {element_invalid}")