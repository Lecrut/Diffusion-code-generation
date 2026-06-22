class ListAccessor:
    def __init__(self, data):
        self._data = data

    def get_tail(self):
        slice_result = self._data[-1:]
        return slice_result[0]

if __name__ == '__main__':
    my_list = [100, 200, 300]
    accessor = ListAccessor(my_list)
    result = accessor.get_tail()
    print(result)