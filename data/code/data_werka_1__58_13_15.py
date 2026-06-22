class ListHandler:
    def __init__(self, data):
        self._data = data

    def _validate_data(self):
        if not isinstance(self._data, list):
            raise ValueError("Provided data is not a list.")
        if len(self._data) == 0:
            raise IndexError("List is empty.")

    def get_first_element(self):
        self._validate_data()
        return self._data[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    handler = ListHandler(sample_list)
    first_element = handler.get_first_element()
    print(first_element)