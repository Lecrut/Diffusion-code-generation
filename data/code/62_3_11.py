class ElementFetcher:
    DEFAULT_LIST = [5, 10, 15, 20]

    def __init__(self, data=None):
        if data is None:
            self._internal_list = self.DEFAULT_LIST
        else:
            self._internal_list = list(data)

    @classmethod
    def fetch_second_element(cls, instance):
        if len(instance._internal_list) > 1:
            return instance._internal_list[1]
        return None

if __name__ == '__main__':
    sample_data = [25, 30, 35, 40]
    fetcher = ElementFetcher(sample_data)
    print(ElementFetcher.fetch_second_element(fetcher))

    default_fetcher = ElementFetcher()
    print(ElementFetcher.fetch_second_element(default_fetcher))