class IndexAccessor:

    def __init__(self):
        self.index_map = {'first': 0, 'second': 1, 'third': 2, 'fourth': 3, 'fifth': 4}

    def get_element(self, data_list, index_or_name):
        if isinstance(index_or_name, str) and index_or_name in self.index_map:
            index = self.index_map[index_or_name]
        else:
            index = index_or_name
        if not isinstance(data_list, list):
            raise TypeError('The first argument must be a list.')
        if not isinstance(index, int):
            raise TypeError('The index must be an integer.')
        try:
            return data_list[index]
        except IndexError:
            raise IndexError('Index out of bounds.')
if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(accessor.get_element(sample_list, 'second'))
        print(accessor.get_element(sample_list, 3))
        print(accessor.get_element(sample_list, 5))
    except Exception as e:
        print(e)