class ItemCounter:

    def __init__(self, initial_data=None):
        if initial_data is None:
            self.counts = {}
        else:
            self.counts = {item: max(0, count) for item, count in initial_data.items()}

    def update_counts(self, updates):
        for item, count in updates.items():
            if not isinstance(count, int) or count < 0:
                raise ValueError('Count must be a non-negative integer')
            if item in self.counts:
                self.counts[item] += count
            else:
                self.counts[item] = count

    def get_unique_item_count(self):
        return len(self.counts)
if __name__ == '__main__':
    counter = ItemCounter({'apple': 3, 'banana': 2})
    print(counter.get_unique_item_count())
    try:
        counter.update_counts({'apple': -1, 'orange': 5})
    except ValueError as e:
        print(e)
    print(counter.get_unique_item_count())