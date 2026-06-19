class ListHandler:
    def __init__(self, data):
        self._data = data

    def fetch_first(self):
        if not self._data:
            raise ValueError("The list is empty.")
        return self._data[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    handler = ListHandler(sample_list)
    try:
        first_element = handler.fetch_first()
        print(first_element)
    except ValueError as e:
        print(f"Error: {e}")