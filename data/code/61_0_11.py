class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        try:
            return self.data_list[index]
        except IndexError:
            return "Index out of bounds"

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_data)
    valid_index = 2
    invalid_index = 5

    element_valid = accessor.get_element(valid_index)
    element_invalid = accessor.get_element(invalid_index)

    print(f"List: {sample_data}")
    print(f"Element at index {valid_index}: {element_valid}")
    print(f"Element at index {invalid_index}: {element_invalid}")