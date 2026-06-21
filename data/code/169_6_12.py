from collections import defaultdict

class ItemCounter:
    def __init__(self):
        self.counts = defaultdict(int)

    def update_count(self, item_id, change):
        self.counts[item_id] += change

    def get_non_zero_items(self):
        return {item: count for item, count in self.counts.items() if count > 0}

    def reset(self):
        self.counts.clear()

    def clone(self):
        new_counter = ItemCounter()
        new_counter.counts.update(self.counts)
        return new_counter

if __name__ == '__main__':
    counter = ItemCounter()
    counter.update_count(101, 5)
    print(f"Count for 101 after first update: {counter.get_non_zero_items()}")
    counter.update_count(101, -2)
    print(f"Count for 101 after second update: {counter.get_non_zero_items()}")
    counter.update_count(202, 10)
    print(f"Count for 202: {counter.get_non_zero_items()}")
    counter.update_count(101, 100)
    print(f"Count for 101 after third update: {counter.get_non_zero_items()}")

    clone = counter.clone()
    clone.reset()
    print(f"Cloned and reset counts: {clone.get_non_zero_items()}")