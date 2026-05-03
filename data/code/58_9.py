class CustomListWrapper:
    def __init__(self, data):
        self._data = data
    def get_first_element(self):
        if not self._data:
            return None
        return self._data[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    wrapper = CustomListWrapper(sample_list)
    first = wrapper.get_first_element()
    print(first)
    empty_wrapper = CustomListWrapper([])
    first_empty = empty_wrapper.get_first_element()
    print(first_empty)