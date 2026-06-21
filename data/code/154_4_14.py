class ItemCounter:
    def __init__(self, iterable):
        self.iterable = iterable

    @staticmethod
    def _increment_count():
        return 1

    def item_count_pairs(self):
        count = 0
        for item in self.iterable:
            yield item, count
            count += self._increment_count()

if __name__ == '__main__':
    sample_list = ['x', 'y', 'z', 'w']
    counter = ItemCounter(sample_list)
    for item, count in counter.item_count_pairs():
        print(f'Item: {item}, Count: {count}')