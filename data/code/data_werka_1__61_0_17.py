class ListAccessor:
    DEFAULT_ERROR_MESSAGE = "Index out of bounds"

    @staticmethod
    def get_element(data_list, index):
        try:
            return data_list[index]
        except IndexError:
            return ListAccessor.DEFAULT_ERROR_MESSAGE

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 7
    result_valid = ListAccessor.get_element(sample_list, valid_index)
    result_invalid = ListAccessor.get_element(sample_list, invalid_index)
    print(f"List: {sample_list}")
    print(f"Element at index {valid_index}: {result_valid}")
    print(f"Element at index {invalid_index}: {result_invalid}")