class IndexAccessor:
    def get_element(self, data_list, index):
        self._validate_data_list(data_list)
        self._validate_index(index, len(data_list))
        return data_list[index]

    def _validate_data_list(self, data_list):
        if not isinstance(data_list, list):
            raise TypeError("The first argument must be a list.")

    def _validate_index(self, index, length):
        if not isinstance(index, int):
            raise TypeError("The index must be an integer.")
        if index < 0 or index >= length:
            raise IndexError("Index out of bounds.")

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    try:
        element = accessor.get_element(sample_list, 2)
        print(f"Element at index 2: {element}")
    except Exception as e:
        print(e)

    try:
        element = accessor.get_element(sample_list, 5)
        print(f"Element at index 5: {element}")
    except Exception as e:
        print(e)