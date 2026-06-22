class ListHandler:
    def __init__(self, elements):
        self.elements = elements
    def fetch_last(self):
        return self.elements[-1] if self.elements else None

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    handler = ListHandler(sample_data)
    last_value = handler.fetch_last()
    print(last_value)