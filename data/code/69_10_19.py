class IndexAccessor:
    def get_element(self, data_list, index):
        if -len(data_list) <= index < len(data_list):
            return data_list[index]
        else:
            raise IndexError('Index out of bounds')

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [1000, 2000, 3000, 4000, 5000]
    try:
        print("Element at index 2:", accessor.get_element(sample_list, 2))
        print("Element at index -1 (last element):", accessor.get_element(sample_list, -1))
        print("Attempting to access element at index 5 (out of bounds):")
        print(accessor.get_element(sample_list, 5))
    except IndexError as e:
        print(e)