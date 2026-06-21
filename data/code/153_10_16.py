class ListSearcher:
    def __init__(self, data_list):
        self.data_list = data_list

    def check_item_exists(self, item):
        return item in self.data_list

if __name__ == '__main__':
    searcher1 = ListSearcher([1, 2, 3, 4, 5])
    print(f"Does 3 exist in the list? {searcher1.check_item_exists(3)}")
    print(f"Does 'apple' exist in the list? {searcher1.check_item_exists('apple')}")
    searcher2 = ListSearcher([10, 20, 30])
    print(f"Does 5 exist in the list? {searcher2.check_item_exists(5)}")
    print(f"Does 10 exist in the list? {searcher2.check_item_exists(10)}")
    searcher3 = ListSearcher([])
    print(f"Does 1 exist in an empty list? {searcher3.check_item_exists(1)}")