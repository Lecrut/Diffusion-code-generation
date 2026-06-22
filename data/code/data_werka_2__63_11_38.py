def get_first_item(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('The iterable is empty')

class FirstItemFetcher:
    def __init__(self, data):
        self.data = data
    def fetch(self):
        return get_first_item(self.data)

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (40, 50, 60)
    sample_string = 'hello'
    
    fetcher_list = FirstItemFetcher(sample_list)
    fetcher_tuple = FirstItemFetcher(sample_tuple)
    fetcher_string = FirstItemFetcher(sample_string)
    
    print(fetcher_list.fetch())
    print(fetcher_tuple.fetch())
    print(fetcher_string.fetch())