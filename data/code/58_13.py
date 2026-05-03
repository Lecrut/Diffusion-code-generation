class ListAccessor:
    def __init__(self, data):
        self._internal_list = data
    def get_first_element(self):
        if not self._internal_list:
            return None
        return self._internal_list[0]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    accessor = ListAccessor(sample_data)
    first_element = accessor.get_first_element()
    print(first_element)