class ListAccessor:
    def __init__(self, initial_list):
        self._data = initial_list
    def get_first_element(self):
        if not self._data:
            raise IndexError("List is empty")
        return self._data[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    accessor = ListAccessor(sample_list)
    first_element = accessor.get_first_element()
    print(first_element)