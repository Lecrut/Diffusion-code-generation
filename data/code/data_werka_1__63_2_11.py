class FirstElementFetcher:
    def __init__(self, data):
        self.data = data

    def fetch(self):
        return self.data[0]

if __name__ == '__main__':
    sample_sequence = [100, 200, 300, 400]
    fetcher = FirstElementFetcher(sample_sequence)
    print(fetcher.fetch())