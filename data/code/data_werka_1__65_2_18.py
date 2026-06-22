class ListElementFetcher:

    def __init__(self, data):
        self._data = data

    def fetch_third_element(self):
        if len(self._data) > 2:
            return self._data[2]
        raise IndexError('List does not have a third element')
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    fetcher = ListElementFetcher(sample_list)
    try:
        third_element = fetcher.fetch_third_element()
        print(f'The third element is: {third_element}')
        invalid_fetch = fetcher.fetch_third_element()
        print(f'This will not be printed: {invalid_fetch}')
    except IndexError as e:
        print(e)