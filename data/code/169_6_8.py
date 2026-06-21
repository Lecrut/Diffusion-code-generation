from collections import defaultdict

class ItemCounter:

    def __init__(self):
        self.counts = defaultdict(int)

    def get_items_with_count(self):
        return {item: count for item, count in self.counts.items() if count > 0}

    def reset(self):
        self.counts.clear()

    def clone(self):
        new_counter = ItemCounter()
        new_counter.counts.update(self.counts)
        return new_counter
if __name__ == '__main__':
    counter = ItemCounter()
    counter.counts['apple'] = 3
    counter.counts['banana'] = 0
    print(counter.get_items_with_count())
    counter.reset()
    print(counter.get_items_with_count())
    cloned_counter = counter.clone()
    print(cloned_counter.get_items_with_count())