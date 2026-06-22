def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]

class ItemFetcher:
    def __init__(self, data_list):
        self.data_list = data_list
    
    def fetch_second(self):
        return get_second_item(self.data_list)

if __name__ == '__main__':
    SAMPLE_LIST_1 = [10, 20, 30, 40, 50]
    SAMPLE_LIST_2 = [5]
    SAMPLE_LIST_3 = ['apple', 'banana', 'cherry']
    SAMPLE_LIST_4 = []

    fetcher_1 = ItemFetcher(SAMPLE_LIST_1)
    fetcher_2 = ItemFetcher(SAMPLE_LIST_2)
    fetcher_3 = ItemFetcher(SAMPLE_LIST_3)
    fetcher_4 = ItemFetcher(SAMPLE_LIST_4)

    print(fetcher_1.fetch_second())
    print(fetcher_2.fetch_second())
    print(fetcher_3.fetch_second())
    print(fetcher_4.fetch_second())