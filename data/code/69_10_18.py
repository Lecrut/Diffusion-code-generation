class IndexAccessor:
    def get_element(self, data_list, index):
        if not isinstance(data_list, list) or not isinstance(index, int):
            raise ValueError('Invalid input types')
        if index >= len(data_list) or index < -len(data_list):
            raise IndexError('Index out of bounds')
        return data_list[index]

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [100, 200, 300, 400, 500]
    print("Element at index 2:", accessor.get_element(sample_list, 2))
    print("Element at index -1 (last element):", accessor.get_element(sample_list, -1))
    try:
        print("Attempting to access element at index 5 (out of bounds):")
        print(accessor.get_element(sample_list, 5))
    except IndexError as e:
        print(e)