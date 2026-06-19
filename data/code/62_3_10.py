class ElementFetcher:
    def __init__(self, items):
        self._items = list(items)

    @classmethod
    def fetch_second(cls, instance):
        if len(instance._items) < 2:
            return None
        return instance._items[1]

if __name__ == '__main__':
    sample_items = [100, 200, 300, 400]
    fetcher = ElementFetcher(sample_items)
    print(ElementFetcher.fetch_second(fetcher))
    
    short_items = [50]
    short_fetcher = ElementFetcher(short_items)
    print(ElementFetcher.fetch_second(short_fetcher))