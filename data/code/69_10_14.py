class IndexAccessor:
    def is_valid_index(self, data_list, index):
        return 0 <= index < len(data_list)

    def get_element(self, data_list, index):
        if self.is_valid_index(data_list, index):
            return data_list[index]
        else:
            raise IndexError('Index out of bounds')

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [100, 200, 300, 400, 500]
    try:
        print("Element at index 2:", accessor.get_element(sample_list, 2))
        print("Attempting to access element at index 5 (out of bounds):")
        print(accessor.get_element(sample_list, 5))
    except IndexError as e:
        print(e)