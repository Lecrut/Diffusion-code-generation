class ListAccessor:
    def __init__(self, data):
        self._data = data
    def get_first_element(self):
        if not self._data:
            return None
        return self._data[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    accessor = ListAccessor(sample_list)
    first = accessor.get_first_element()
    print(first)
    empty_accessor = ListAccessor([])
    first_empty = empty_accessor.get_first_element()
    print(first_empty)