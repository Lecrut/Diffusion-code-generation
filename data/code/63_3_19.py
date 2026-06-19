class ListProcessor:
    def __init__(self, items):
        self._items = items

    def get_first_element(self):
        return self._items[0] if self._items else None

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    processor = ListProcessor(sample_list)
    print(processor.get_first_element())

    empty_list = []
    empty_processor = ListProcessor(empty_list)
    print(empty_processor.get_first_element())