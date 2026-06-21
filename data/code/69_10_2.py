class IndexAccessor:

    def __init__(self):
        self.index_map = {'first': 0, 'second': 1, 'third': 2, 'fourth': 3, 'fifth': 4}

    def get_element(self, data_list, index_or_name):
        if isinstance(index_or_name, str) and index_or_name in self.index_map:
            index = self.index_map[index_or_name]
        else:
            index = index_or_name
        if index < 0 or index >= len(data_list):
            raise IndexError('Index out of bounds')
        return data_list[index]
if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(accessor.get_element(sample_list, 'third'))
        print(accessor.get_element(sample_list, 4))
        print(accessor.get_element(sample_list, 5))
    except IndexError as e:
        print(e)