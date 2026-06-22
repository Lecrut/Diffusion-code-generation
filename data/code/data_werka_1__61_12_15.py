class SafeElementFetcher:
    def __init__(self, data):
        self._data = data

    @classmethod
    def fetch(cls, instance, position):
        if 0 <= position < len(instance._data):
            return instance._data[position]
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [1000, 2000, 3000, 4000, 5000]
    fetcher = SafeElementFetcher(SAMPLE_LIST)
    print(SafeElementFetcher.fetch(fetcher, 2))
    print(SafeElementFetcher.fetch(fetcher, 0))
    print(SafeElementFetcher.fetch(fetcher, -1))
    print(SafeElementFetcher.fetch(fetcher, 5))