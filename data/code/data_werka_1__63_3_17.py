class ElementFetcher:
    def __init__(self, data):
        self._data_store = data

    def fetch_first_element(self):
        if not self._data_store:
            return None
        return self._data_store[0]

if __name__ == '__main__':
    sample_values = {'list1': [5, 15, 25], 'list2': [], 'list3': [35, 45]}
    for key, value in sample_values.items():
        fetcher = ElementFetcher(value)
        first_element = fetcher.fetch_first_element()
        print(f"First element of {key}: {first_element}")