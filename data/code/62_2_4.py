class ElementFetcher:
    def __init__(self, elements):
        self.elements = elements
    def fetch_second(self):
        if len(self.elements) < 2:
            raise IndexError("List does not contain at least two elements.")
        return self.elements[1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    fetcher = ElementFetcher(sample_list)
    print(fetcher.fetch_second())