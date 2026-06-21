class ItemCounter:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def get_next_item_count_pair(self):
        try:
            item = next(self.iterable)
            pair = (item, self.count)
            self.count += 1
            return pair
        except StopIteration:
            raise StopIteration("No more items to process")

if __name__ == '__main__':
    sample_list = ['x', 'y', 'z']
    counter = ItemCounter(sample_list)
    
    print(counter.get_next_item_count_pair())
    print(counter.get_next_item_count_pair())
    print(counter.get_next_item_count_pair())