class ListAccessor:
    @staticmethod
    def get_element_by_position(data_list, index):
        try:
            return data_list[index]
        except IndexError as e:
            raise IndexError(f"Index {index} is out of bounds: {e}")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    index_to_access = 2
    try:
        value = ListAccessor.get_element_by_position(sample_data, index_to_access)
        print(f"Element at index {index_to_access}: {value}")
    except IndexError as e:
        print(e)

    invalid_index = 5
    try:
        value = ListAccessor.get_element_by_position(sample_data, invalid_index)
        print(f"Element at index {invalid_index}: {value}")
    except IndexError as e:
        print(e)

    negative_index = -1
    try:
        value = ListAccessor.get_element_by_position(sample_data, negative_index)
        print(f"Element at index {negative_index}: {value}")
    except IndexError as e:
        print(e)