class ListHandler:
    def __init__(self, data):
        self.data = data

    def fetch_first(self):
        if not self.data:
            return None
        return self.data[0]

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35]
    handler = ListHandler(sample_values)
    first_element = handler.fetch_first()
    print(first_element)

    empty_values = []
    empty_handler = ListHandler(empty_values)
    first_empty = empty_handler.fetch_first()
    print(first_empty)