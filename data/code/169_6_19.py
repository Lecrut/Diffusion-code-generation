from collections import defaultdict

class ItemCounter:

    def __init__(self):
        self.counts = defaultdict(int)

    def get_counts(self):
        return {item: count for item, count in self.counts.items() if count > 0}

    def reset(self):
        self.counts.clear()

    def clone(self):
        new_counter = ItemCounter()
        new_counter.counts.update(self.counts)
        return new_counter
if __name__ == '__main__':
    counter = ItemCounter()
    counter.counts['apple'] += 3
    counter.counts['banana'] += 1
    print(counter.get_counts())
    clone_counter = counter.clone()
    clone_counter.counts['orange'] += 2
    print(clone_counter.get_counts())
    counter.reset()
    print(counter.get_counts())