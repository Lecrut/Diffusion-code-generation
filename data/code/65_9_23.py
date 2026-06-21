class ListAccessor:

    def __init__(self, initial_list=None):
        if initial_list is None:
            self._list = []
        else:
            self._list = initial_list

    def get(self, index):
        try:
            return self._list[index]
        except IndexError:
            raise ValueError('Index out of range')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    print(accessor.get(2))
    try:
        print(accessor.get(10))
    except ValueError as e:
        print(e)