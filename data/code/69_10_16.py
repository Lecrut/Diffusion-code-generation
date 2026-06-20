class IndexAccessor:
    def get_element(self, data_list, index):
        if not isinstance(data_list, list) or not all(isinstance(x, int) for x in data_list):
            raise ValueError('data_list must be a list of integers')
        if not isinstance(index, int):
            raise ValueError('index must be an integer')
        if 0 <= index < len(data_list):
            return data_list[index]
        else:
            raise IndexError('Index out of bounds')

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [100, 200, 300, 400, 500]
    try:
        print("Element at index 2:", accessor.get_element(sample_list, 2))
        print("Attempting to access element at index -1 (out of bounds):")
        print(accessor.get_element(sample_list, -1))
        print("Attempting to access invalid data type:")
        print(accessor.get_element('not a list', 0))
    except (IndexError, ValueError) as e:
        print(e)