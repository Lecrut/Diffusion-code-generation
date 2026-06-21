from collections import defaultdict

class ItemCounter:
    def __init__(self):
        self.counts = defaultdict(int)

    def increment(self, item):
        self.counts[item] += 1

    def get_items_with_count_greater_than_zero(self):
        return {item: count for item, count in self.counts.items() if count > 0}

    def reset(self):
        self.counts.clear()

    def clone(self):
        new_counter = ItemCounter()
        new_counter.counts.update(self.counts)
        return new_counter

if __name__ == '__main__':
    counter = ItemCounter()
    counter.increment('apple')
    counter.increment('banana')
    print(counter.get_items_with_count_greater_than_zero())
    counter.reset()
    print(counter.get_items_with_count_greater_than_zero())
    cloned_counter = counter.clone()
    cloned_counter.increment('orange')
    print(cloned_counter.get_items_with_count_greater_than_zero())