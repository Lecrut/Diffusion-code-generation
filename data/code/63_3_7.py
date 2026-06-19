class ListHandler:
    def __init__(self, elements):
        self._elements = elements

    def fetch_first(self):
        return self._elements[0] if self._elements else None

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    handler = ListHandler(sample_list)
    first_element = handler.fetch_first()
    print(first_element)

    empty_list = []
    empty_handler = ListHandler(empty_list)
    first_from_empty = empty_handler.fetch_first()
    print(first_from_empty)