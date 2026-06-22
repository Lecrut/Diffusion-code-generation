class ListFetcher:
    def __init__(self, items):
        self._items = items

    def fetch_first(self):
        if not self._items:
            raise IndexError("The list is empty and has no first element.")
        return self._items[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    fetcher = ListFetcher(sample_list)
    try:
        first_element = fetcher.fetch_first()
        print(first_element)
    except IndexError as e:
        print(f"Error: {e}")

    empty_list = []
    empty_fetcher = ListFetcher(empty_list)
    try:
        empty_first_element = empty_fetcher.fetch_first()
        print(empty_first_element)
    except IndexError as e:
        print(f"Error: {e}")