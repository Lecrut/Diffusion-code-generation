class UniqueItemCollector:
    def __init__(self):
        self._seen = set()
        self._result = []

    def add_item(self, item_name):
        if item_name not in self._seen:
            self._seen.add(item_name)
            self._result.append(item_name)

    def get_items(self):
        return self._result

if __name__ == '__main__':
    collector = UniqueItemCollector()
    collector.add_item("apple")
    collector.add_item("banana")
    collector.add_item("apple")
    collector.add_item("orange")
    items = collector.get_items()
    print(items)