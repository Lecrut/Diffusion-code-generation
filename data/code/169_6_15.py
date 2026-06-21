from collections import defaultdict

class ItemCounter:
    def __init__(self):
        self.counts = defaultdict(int)

    def update(self, item_id, change):
        self.counts[item_id] += change

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
    counter.update(101, 5)
    print(f"Count for 101 after first update: {counter.get_counts().get(101)}")
    counter.update(101, -2)
    print(f"Count for 101 after second update: {counter.get_counts().get(101)}")
    counter.update(202, 10)
    print(f"Count for 202: {counter.get_counts().get(202)}")
    counter.update(101, 100)
    print(f"Count for 101 after third update: {counter.get_counts().get(101)}")

    cloned_counter = counter.clone()
    cloned_counter.update(202, -5)
    print(f"Original count for 202: {counter.get_counts().get(202)}")
    print(f"Cloned count for 202: {cloned_counter.get_counts().get(202)}")

    counter.reset()
    print(f"After reset, count for 101: {counter.get_counts().get(101)}")