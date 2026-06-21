class ListAccessor:
    def __init__(self, data):
        self._data = data

    def get_second_to_last(self):
        return self._data[-2]

if __name__ == '__main__':
    sample_list = [5, 12, 8, 23, 7, 99]
    accessor = ListAccessor(sample_list)
    print(accessor.get_second_to_last())