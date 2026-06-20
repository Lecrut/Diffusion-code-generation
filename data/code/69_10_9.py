class IndexAccessor:
    MAX_INDEX_ERROR = 'Index out of bounds'

    @staticmethod
    def _is_valid_index(index, length):
        return 0 <= index < length

    def get_element(self, data_list, index):
        if self._is_valid_index(index, len(data_list)):
            return data_list[index]
        else:
            raise IndexError(self.MAX_INDEX_ERROR)

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [100, 200, 300, 400, 500]
    try:
        print("Element at index 2:", accessor.get_element(sample_list, 2))
        print("Attempting to access element at index 5 (out of bounds):")
        print(accessor.get_element(sample_list, 5))
    except IndexError as e:
        print(e)