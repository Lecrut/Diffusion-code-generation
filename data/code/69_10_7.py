class IndexAccessor:
    def get_element(self, data_list, index):
        if not isinstance(data_list, list) or not isinstance(index, int):
            raise ValueError('Invalid input type')
        if 0 <= index < len(data_list):
            return data_list[index]
        else:
            raise IndexError('Index out of bounds')

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [1, 2, 3, 4, 5]
    try:
        print("Element at index 2:", accessor.get_element(sample_list, 2))
        print("Attempting to access element at index -1 (out of bounds):")
        print(accessor.get_element(sample_list, -1))
    except IndexError as e:
        print(e)