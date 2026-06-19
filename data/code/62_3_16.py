class ElementFetcher:
    DEFAULT_LIST_LENGTH = 2

    def __init__(self, data):
        self._data_list = list(data)

    @classmethod
    def get_second_element(cls, instance):
        if len(instance._data_list) >= cls.DEFAULT_LIST_LENGTH:
            return instance._data_list[1]
        return None

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20]
    fetcher = ElementFetcher(sample_data)
    print(ElementFetcher.get_second_element(fetcher))
    
    short_data = [30]
    short_fetcher = ElementFetcher(short_data)
    print(ElementFetcher.get_second_element(short_fetcher))