class IndexAccessor:
    def get_element(self, data_list, index):
        if not isinstance(data_list, list):
            raise TypeError("The first argument must be a list.")
        if not isinstance(index, int):
            raise TypeError("The index must be an integer.")
        try:
            return data_list[index]
        except IndexError:
            raise IndexError("Index out of bounds.")

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_data = [5, 15, 25, 35, 45]
    index_to_retrieve = 2
    try:
        element_at_index = accessor.get_element(sample_data, index_to_retrieve)
        print(f"Element at index {index_to_retrieve}: {element_at_index}")
    except IndexError as e:
        print(e)