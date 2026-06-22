class ListElementFetcher:

    def __init__(self, data):
        self._data = list(data)

    def fetch(self, index):
        if -len(self._data) <= index < len(self._data):
            return self._data[index]
        raise IndexError('Index out of bounds')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    fetcher = ListElementFetcher(sample_list)
    print(fetcher.fetch(0))
    print(fetcher.fetch(2))
    print(fetcher.fetch(-1))
    try:
        print(fetcher.fetch(5))
    except IndexError as e:
        print(e)
    try:
        print(fetcher.fetch(-6))
    except IndexError as e:
        print(e)