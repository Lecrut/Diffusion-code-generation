class LastItemFetcher:
    def __init__(self, items):
        self.items = items

    def fetch(self):
        if not self.items:
            raise IndexError("Cannot retrieve last element from an empty list")
        return self.items[-1]

if __name__ == '__main__':
    sample_list = [7, 17, 27, 37, 47]
    fetcher = LastItemFetcher(sample_list)
    print(fetcher.fetch())