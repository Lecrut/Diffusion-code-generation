class ListHandler:
    def __init__(self, data):
        self._data = data

    def is_empty(self):
        return len(self._data) == 0

    def get_first_element(self):
        if self.is_empty():
            return None
        return self._data[0]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35]
    handler = ListHandler(sample_data)
    first_element = handler.get_first_element()
    print(first_element)