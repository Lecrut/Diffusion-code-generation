class IndexAccessor:
    def get_element(self, data_list, index):
        if not isinstance(data_list, list):
            raise TypeError("The first argument must be a list.")
        if not isinstance(index, int):
            raise TypeError("The index must be an integer.")
        try:
            return data_list[index]
        except IndexError:
            raise IndexError(f"Index {index} is out of bounds for the list.")

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 3
    try:
        element = accessor.get_element(sample_list, index_to_access)
        print(f"Element at index {index_to_access}: {element}")
    except Exception as e:
        print(e)