class UniqueItemCollector:
    def __init__(self):
        self._items = []

    def add_items(self, names):
        for name in names:
            if name not in self._items:
                self._items.append(name)

    def get_all_names(self):
        return self._items

if __name__ == '__main__':
    collector = UniqueItemCollector()
    sample_names_1 = ["Apple", "Banana", "Cherry"]
    sample_names_2 = ["Date", "Elderberry", "Apple"]
    collector.add_items(sample_names_1)
    collector.add_items(sample_names_2)
    retrieved_names = collector.get_all_names()
    print(retrieved_names)