class UniqueItemCollector:
    def __init__(self):
        self._seen = set()
        self._unique_items = []

    def add_item(self, item_name):
        if item_name not in self._seen:
            self._seen.add(item_name)
            self._unique_items.append(item_name)

    def get_unique_items(self):
        return list(self._unique_items)

if __name__ == '__main__':
    collector = UniqueItemCollector()
    collector.add_item("apple")
    collector.add_item("banana")
    collector.add_item("apple")
    collector.add_item("orange")
    collector.add_item("banana")
    collector.add_item("grape")
    
    unique_items = collector.get_unique_items()
    print(unique_items)