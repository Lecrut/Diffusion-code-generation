def first_element_generator(input_list):
    if input_list:
        yield input_list[0]

class FirstElementFetcher:
    def __init__(self, iterable):
        self.iterable = iterable

    def fetch_first(self):
        try:
            return next(first_element_generator(self.iterable))
        except StopIteration:
            return None

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400]
    fetcher = FirstElementFetcher(sample_list)
    print(fetcher.fetch_first())

    empty_list = []
    empty_fetcher = FirstElementFetcher(empty_list)
    print(empty_fetcher.fetch_first())