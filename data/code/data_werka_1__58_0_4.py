class ElementFetcher:

    def __init__(self, elements):
        self.elements = elements

    def fetch_first(self):
        if not self.elements:
            raise IndexError('The list is empty.')
        return self.elements[0]
if __name__ == '__main__':
    sample_list = [5, 10, 15, 20]
    fetcher = ElementFetcher(sample_list)
    first_element = fetcher.fetch_first()
    print(first_element)