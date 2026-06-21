class IndexAccessor:
    def get_element(self, data_list, index):
        try:
            return data_list[index]
        except IndexError:
            raise IndexError("Index out of bounds")

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 3
    try:
        element = accessor.get_element(sample_list, index_to_access)
        print(f"Element at index {index_to_access}: {element}")
    except IndexError as e:
        print(e)