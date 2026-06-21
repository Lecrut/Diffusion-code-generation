class IndexAccessor:

    def get_element(self, data_list, index):
        self.validate_input(data_list, index)
        try:
            return data_list[index]
        except IndexError:
            raise IndexError('Index out of bounds.')

    def validate_input(self, data_list, index):
        if not isinstance(data_list, list):
            raise TypeError('The first argument must be a list.')
        if not isinstance(index, int):
            raise TypeError('The index must be an integer.')
if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [100, 200, 300, 400, 500]
    try:
        print(accessor.get_element(sample_list, 1))
        print(accessor.get_element(sample_list, 5))
    except Exception as e:
        print(e)