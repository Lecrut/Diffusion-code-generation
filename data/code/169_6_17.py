from collections import defaultdict

class ItemCounter:
    def __init__(self):
        self.counts = defaultdict(int)

    def get_positive_counts(self):
        return {item: count for item, count in self.counts.items() if count > 0}

    def reset(self):
        self.counts.clear()

    def clone(self):
        new_counter = ItemCounter()
        new_counter.counts.update(self.counts)
        return new_counter

if __name__ == '__main__':
    counter = ItemCounter()
    counter.counts[101] += 5
    print(f"Count for 101 after first update: {counter.get_positive_counts().get(101)}")
    counter.counts[101] -= 2
    print(f"Count for 101 after second update: {counter.get_positive_counts().get(101)}")
    counter.counts[202] += 10
    print(f"Count for 202: {counter.get_positive_counts().get(202)}")
    counter.counts[101] += 100
    print(f"Count for 101 after third update: {counter.get_positive_counts().get(101)}")

    reset_counter = counter.clone()
    reset_counter.reset()
    print(f"After cloning and resetting, count for 101: {reset_counter.get_positive_counts().get(101)}")