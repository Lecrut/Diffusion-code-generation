class IndexAccessor:
    def get_element(self, data_list, index):
        if index < 0 or index >= len(data_list):
            raise IndexError('Index out of bounds')
        return data_list[index]

if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    
    try:
        print("Element at index 2:", accessor.get_element(sample_list, 2))
        print("Element at index -1 (last element):", accessor.get_element(sample_list, -1))
        print("Element at index 5 (should raise an error):", accessor.get_element(sample_list, 5))
    except IndexError as e:
        print(e)