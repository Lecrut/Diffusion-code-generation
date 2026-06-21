class InventoryController:
    __slots__ = ('_items',)
    
    def __init__(self):
        self._items = {}
    
    def add_item(self, category, item):
        if category not in self._items:
            self._items[category] = []
        self._items[category].append(item)
    
    def filter_items_by_category(self, category):
        return (item for item in self._items.get(category, []))

if __name__ == '__main__':
    controller = InventoryController()
    controller.add_item('electronics', 'Laptop')
    controller.add_item('accessories', 'Mouse')
    controller.add_item('accessories', 'Keyboard')
    print(list(controller.filter_items_by_category('accessories')))