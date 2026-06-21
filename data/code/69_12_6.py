class ListElementAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        try:
            return self.data_list[index]
        except IndexError:
            raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = ListElementAccessor(sample_data)

    try:
        print(f"Element at index 2: {accessor.get_element(2)}")
        print(f"Element at index -1: {accessor.get_element(-1)}")
        invalid_index_access = accessor.get_element(5)
    except IndexError as e:
        print(f"Caught expected error: {e}")