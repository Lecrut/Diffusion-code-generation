class SafeElementFetcher:
    def __init__(self, data):
        self.data = data

    @classmethod
    def fetch_element(cls, instance, index):
        return instance.data.get(index) if 0 <= index < len(instance.data) else None

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    data_dict = {i: value for i, value in enumerate(sample_data)}
    fetcher = SafeElementFetcher(data_dict)
    print(SafeElementFetcher.fetch_element(fetcher, 2))
    print(SafeElementFetcher.fetch_element(fetcher, 0))
    print(SafeElementFetcher.fetch_element(fetcher, 5))
    print(SafeElementFetcher.fetch_element(fetcher, -1))