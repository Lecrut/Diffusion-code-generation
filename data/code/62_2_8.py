class ElementFetcher:
    def __init__(self, elements):
        self.elements = elements
    def fetch_second(self):
        return self.elements[1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    fetcher = ElementFetcher(sample_list)
    print(fetcher.fetch_second())