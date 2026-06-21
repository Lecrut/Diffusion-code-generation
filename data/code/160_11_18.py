class UniqueItemCollector:
    def __init__(self):
        self._item_set = set()
        self._item_list = []
    
    def add_item(self, item_name):
        if item_name not in self._item_set:
            self._item_set.add(item_name)
            self._item_list.append(item_name)
    
    def get_unique_items(self):
        return self._item_list

if __name__ == '__main__':
    collector = UniqueItemCollector()
    collector.add_item("apple")
    collector.add_item("banana")
    collector.add_item("apple")
    collector.add_item("orange")
    items = collector.get_unique_items()
    print(items)