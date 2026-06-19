class ElementFetcher:
    def __init__(self, elements):
        self._elements = list(elements)

    @classmethod
    def fetch_second(cls, instance):
        if len(instance._elements) < 2:
            return None
        return instance._elements[1]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20]
    fetcher = ElementFetcher(sample_data)
    print(ElementFetcher.fetch_second(fetcher))
    
    short_data = [30]
    short_fetcher = ElementFetcher(short_data)
    print(ElementFetcher.fetch_second(short_fetcher))