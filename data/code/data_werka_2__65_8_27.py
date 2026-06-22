class SafeListAccess:
    def __init__(self, data_list):
        if not isinstance(data_list, list):
            raise TypeError("The first argument must be a list.")
        self.data_list = data_list

    def get_element_by_position(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        try:
            return self.data_list[index]
        except IndexError:
            raise IndexError(f"Index {index} is out of bounds for the given list.")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    safe_accessor = SafeListAccess(sample_data)
    
    valid_index_1 = 2
    valid_index_2 = 4
    
    try:
        print(f"Element at index {valid_index_1}: {safe_accessor.get_element_by_position(valid_index_1)}")
        print(f"Element at index {valid_index_2}: {safe_accessor.get_element_by_position(valid_index_2)}")
    except IndexError as e:
        print(e)
    
    invalid_index = 5
    try:
        print(get_element_by_position(sample_data, invalid_index))
    except IndexError as e:
        print(e)