class PositionFetcher:
    DEFAULT_INDEX = 0

    @staticmethod
    def fetch_by_position(iterable, index=DEFAULT_INDEX):
        if not isinstance(index, int) or index < 0:
            raise ValueError("Index must be a non-negative integer.")
        for i, item in enumerate(iterable):
            if i == index:
                yield item

if __name__ == '__main__':
    large_list = list(range(1000000))
    target_index = 500000
    try:
        generator = PositionFetcher.fetch_by_position(large_list, target_index)
        result = next(generator, None)
        print(result)
    except ValueError as e:
        print(e)