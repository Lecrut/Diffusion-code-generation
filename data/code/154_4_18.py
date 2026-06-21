class ItemCounter:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
    
    def get_next_item_count(self):
        try:
            item = next(self.iterable)
            count = sum(1 for _ in self.iterable) + 1
            self.iterable = iter([item] + list(self.iterable))
            return item, count
        except StopIteration:
            return None, 0

if __name__ == '__main__':
    sample_list = ['x', 'y', 'z']
    counter = ItemCounter(sample_list)
    print(f'Item: {counter.get_next_item_count()[0]}, Count: {counter.get_next_item_count()[1]}')
    print(f'Item: {counter.get_next_item_count()[0]}, Count: {counter.get_next_item_count()[1]}')
    print(f'Item: {counter.get_next_item_count()[0]}, Count: {counter.get_next_item_count()[1]}')