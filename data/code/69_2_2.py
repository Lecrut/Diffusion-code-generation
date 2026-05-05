class IndexAccessor:
    def __init__(self, data):
        self._data = data
    def get_element(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = IndexAccessor(sample_list)
    print(accessor.get_element(0))
    print(accessor.get_element(2))
    print(accessor.get_element(4))
    print(accessor.get_element(10))
    print(accessor.get_element(-1))