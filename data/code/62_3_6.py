class ElementFetcher:
    DEFAULT_DATA = [100, 200, 300, 400]

    def __init__(self, data=None):
        if data is None:
            self._internal_list = ElementFetcher.DEFAULT_DATA
        else:
            self._internal_list = list(data)

    @classmethod
    def get_second_element(cls, instance):
        return cls._get_safe_element(instance, 1)

    @staticmethod
    def _get_safe_element(instance, index):
        if len(instance._internal_list) > index:
            return instance._internal_list[index]
        return None

if __name__ == '__main__':
    sample_data = [50, 60, 70, 80]
    fetcher = ElementFetcher(sample_data)
    print(ElementFetcher.get_second_element(fetcher))

    default_fetcher = ElementFetcher()
    print(ElementFetcher.get_second_element(default_fetcher))