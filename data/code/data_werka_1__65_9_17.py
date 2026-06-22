class ListAccessor:

    def __init__(self, data_list):
        self.data_list = data_list

    def _validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if index < 0 or index >= len(self.data_list):
            raise IndexError('Position out of bounds')

    def get(self, index):
        self._validate_index(index)
        return self.data_list[index]
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get(2))
        print(accessor.get(0))
        print(accessor.get(4))
        print(accessor.get(-1))
    except (IndexError, TypeError) as e:
        print(f'Error: {e}')