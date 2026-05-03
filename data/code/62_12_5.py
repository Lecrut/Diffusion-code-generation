class ListAccessor:
    def __init__(self, data):
        self._data = data
    def get_second(self):
        if len(self._data) > 1:
            return self._data[1]
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    result = accessor.get_second()
    print(result)
    sample_list_short = [100]
    accessor_short = ListAccessor(sample_list_short)
    result_short = accessor_short.get_second()
    print(result_short)
    sample_list_empty = []
    accessor_empty = ListAccessor(sample_list_empty)
    result_empty = accessor_empty.get_second()
    print(result_empty)