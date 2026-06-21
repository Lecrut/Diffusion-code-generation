class ItemCounter:
    def __init__(self):
        self.counts = {}

    def update_counts(self, new_counts):
        for item, count in new_counts.items():
            if item in self.counts:
                self.counts[item] += count
            else:
                self.counts[item] = count

    def get_unique_items_count(self):
        return len(self.counts)

if __name__ == '__main__':
    counter = ItemCounter()
    counter.update_counts({'apple': 3, 'banana': 2})
    counter.update_counts({'banana': 1, 'orange': 5})
    print(counter.get_unique_items_count())