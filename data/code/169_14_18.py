class ItemCounter:
    def __init__(self, initial_data=None):
        if initial_data is None:
            self.data = {}
        else:
            self.data = {item: count for item, count in initial_data.items()}

    def add_counts(self, updates):
        for item, count in updates.items():
            if item in self.data:
                self.data[item] += count
            else:
                self.data[item] = count

    def get_unique_items_count(self):
        return len(self.data)

if __name__ == '__main__':
    counter = ItemCounter(initial_data={'apple': 3, 'banana': 2})
    counter.add_counts({'apple': 1, 'orange': 5})
    print(counter.get_unique_items_count())