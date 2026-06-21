class IndexAccessor:

    def get_element(self, data_list, index):
        if not isinstance(data_list, list):
            raise TypeError('The first argument must be a list.')
        if not isinstance(index, int):
            raise TypeError('The index must be an integer.')
        if index < 0 or index >= len(data_list):
            raise IndexError('Index out of bounds.')
        return data_list[index]
if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(accessor.get_element(sample_list, 1))
        print(accessor.get_element(sample_list, 5))
    except Exception as e:
        print(e)