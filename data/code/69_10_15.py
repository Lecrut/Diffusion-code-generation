class IndexAccessor:
    MAX_INDEX_ERROR = 'Index exceeds list bounds.'
    MIN_INDEX_ERROR = 'Index is below zero.'

    def get_element(self, data_list, index):
        if index < 0:
            raise IndexError(self.MIN_INDEX_ERROR)
        elif index >= len(data_list):
            raise IndexError(self.MAX_INDEX_ERROR)
        return data_list[index]
if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(accessor.get_element(sample_list, 2))
        print(accessor.get_element(sample_list, -1))
    except IndexError as e:
        print(e)