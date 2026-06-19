class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    @staticmethod
    def _validate_index(index, list_length):
        if index < 0 or index >= list_length:
            raise IndexError("Error: Index out of bounds")

    def get_element(self, index):
        try:
            self._validate_index(index, len(self.data_list))
            return self.data_list[index]
        except IndexError as e:
            return str(e)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    
    valid_index = 2
    invalid_index_high = 5
    invalid_index_low = -1
    
    result_valid = accessor.get_element(valid_index)
    result_invalid_high = accessor.get_element(invalid_index_high)
    result_invalid_low = accessor.get_element(invalid_index_low)
    
    print(f"List: {sample_list}")
    print(f"Element at index {valid_index}: {result_valid}")
    print(f"Attempted access at index {invalid_index_high}: {result_invalid_high}")
    print(f"Attempted access at index {invalid_index_low}: {result_invalid_low}")