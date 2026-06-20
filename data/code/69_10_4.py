class IndexAccessor:
    MIN_INDEX = 0
    MAX_INDEX = float('inf')

    @staticmethod
    def is_valid_index(index, list_length):
        return IndexAccessor.MIN_INDEX <= index < list_length

    def get_element(self, data_list, index):
        if self.is_valid_index(index, len(data_list)):
            return data_list[index]
        else:
            raise IndexError('Index out of bounds')

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    print("Element at index 2:", accessor.get_element(sample_list, 2))
    try:
        print("Attempting to access element at index -1 (out of bounds):")
        print(accessor.get_element(sample_list, -1))
    except IndexError as e:
        print(e)