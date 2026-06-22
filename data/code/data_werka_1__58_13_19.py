class ListHandler:
    def __init__(self, data):
        self._data = data

    def validate_data(self):
        if not isinstance(self._data, list):
            raise TypeError("Data must be a list.")
        if len(self._data) == 0:
            return None
        return self._data[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    handler = ListHandler(sample_list)
    first_element = handler.validate_data()
    print(first_element)

    empty_list_handler = ListHandler([])
    result_for_empty = handler.validate_data()
    print(result_for_empty)