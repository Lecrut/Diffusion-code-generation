from collections import defaultdict

class ItemCounter:
    def __init__(self):
        self.counts = defaultdict(int)

    def update_count(self, item_id, change):
        self.counts[item_id] += change

    def get_positive_counts(self):
        return {item: count for item, count in self.counts.items() if count > 0}

    def reset_counter(self):
        self.counts.clear()

    def clone_counter(self):
        new_instance = ItemCounter()
        new_instance.counts.update(self.counts)
        return new_instance

if __name__ == '__main__':
    counter = ItemCounter()
    counter.update_count(101, 5)
    print(f"Count for 101: {counter.get_positive_counts()[101]}")
    counter.update_count(102, 10)
    print(f"Count for 102: {counter.get_positive_counts()[102]}")
    counter.update_count(101, -2)
    print(f"Count for 101 after decrease: {counter.get_positive_counts().get(101, 0)}")
    counter.reset_counter()
    print(f"After reset: {counter.get_positive_counts()}")
    cloned_counter = counter.clone_counter()
    cloned_counter.update_count(103, 5)
    print(f"Cloned counter for 103: {cloned_counter.get_positive_counts()[103]}")