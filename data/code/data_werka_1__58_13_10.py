class ListHandler:
    def __init__(self, elements):
        self.elements = elements

    def fetch_first(self):
        if not self.elements:
            return None
        return self.elements[0]

    def is_empty(self):
        return len(self.elements) == 0

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    handler = ListHandler(sample_list)
    first_element = handler.fetch_first()
    print(first_element)
    empty_handler = ListHandler([])
    print(empty_handler.is_empty())
    print(empty_handler.fetch_first())