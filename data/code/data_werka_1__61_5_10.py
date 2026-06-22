class PositionalElementFetcher:
    DEFAULT_INDEX = 0

    @staticmethod
    def fetch_element(iterable, position):
        if not isinstance(iterable, (list, tuple)):
            raise TypeError("The iterable must be a list or tuple.")
        if not isinstance(position, int) or position < 0:
            raise ValueError("Position must be a non-negative integer.")
        for index, item in enumerate(iterable):
            if index == position:
                yield item

if __name__ == '__main__':
    large_list = list(range(1000000))
    target_index = 500000
    try:
        fetcher = PositionalElementFetcher()
        element_generator = fetcher.fetch_element(large_list, target_index)
        result = next(element_generator, None)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)