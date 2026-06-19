class PositionFetcher:
    def __init__(self, iterable):
        self.iterable = iterable

    def fetch_by_position(self, position):
        for index, item in enumerate(self.iterable):
            if index == position:
                yield item

if __name__ == '__main__':
    large_list = list(range(1000000))
    target_index = 500000
    fetcher = PositionFetcher(large_list)
    generator = fetcher.fetch_by_position(target_index)
    result = next(generator, None)
    print(result)