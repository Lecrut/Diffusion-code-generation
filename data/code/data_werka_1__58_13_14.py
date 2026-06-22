class ListHandler:
    def __init__(self, data):
        self._data = data

    def get_first_element(self):
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35]
    handler = ListHandler(sample_data)
    first_element = handler.get_first_element()
    print(first_element)
    is_empty_result = handler.is_empty()
    print(is_empty_result)

    empty_data = []
    empty_handler = ListHandler(empty_data)
    first_empty = empty_handler.get_first_element()
    print(first_empty)
    is_empty_empty = empty_handler.is_empty()
    print(is_empty_empty)