class ElementFetcher:
    DEFAULT_LIST = [100, 200, 300, 400]

    def __init__(self, data=None):
        self._internal_list = data if data is not None else self.DEFAULT_LIST

    @classmethod
    def fetch_second(cls, instance):
        return instance._internal_list[1] if len(instance._internal_list) > 1 else None

if __name__ == '__main__':
    sample_data = [50, 60, 70, 80]
    fetcher = ElementFetcher(sample_data)
    result = ElementFetcher.fetch_second(fetcher)
    print(result)

    default_fetcher = ElementFetcher()
    default_result = ElementFetcher.fetch_second(default_fetcher)
    print(default_result)