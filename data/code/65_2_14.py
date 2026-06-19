class ListAccessor:
    def __init__(self, data):
        self._data = data

    def get_third_element(self):
        return self._data[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    print(accessor.get_third_element())