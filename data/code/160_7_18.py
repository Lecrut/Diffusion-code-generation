class UniqueItemCollector:
    def __init__(self):
        self._items = []

    def add_items(self, names):
        for item in names:
            if item not in self._items:
                self._items.append(item)

    def get_all_names(self):
        return self._items

if __name__ == '__main__':
    collector = UniqueItemCollector()
    sample_names_1 = ["Apple", "Banana", "Cherry"]
    sample_names_2 = ["Date", "Elderberry", "Apple"]
    collector.add_items(sample_names_1)
    collector.add_items(sample_names_2)
    all_names = collector.get_all_names()
    print(all_names)