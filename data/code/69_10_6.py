class IndexAccessor:
    def get_element(self, data_list, index):
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
    except IndexError as e:
        print(e)