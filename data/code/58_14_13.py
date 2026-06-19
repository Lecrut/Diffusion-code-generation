class ListElementFetcher:
    def __init__(self, lst):
        self.lst = lst

    def fetch_first_element(self):
        return self.lst[0] if self.lst else None

if __name__ == '__main__':
    sample_lists = [
        [100, 200, 300],
        [],
        ['a', 'b', 'c'],
        [True, False]
    ]
    
    for i, lst in enumerate(sample_lists):
        fetcher = ListElementFetcher(lst)
        print(f"First element of list {i+1}: {fetcher.fetch_first_element()}")