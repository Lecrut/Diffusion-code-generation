class InventoryController:
    __slots__ = ('items',)
    def __init__(self):
        self.items = {}
    def add_item(self, category, item):
        if category not in self.items:
            self.items[category] = []
        self.items[category].append(item)
    def filter_items_by_category(self, category):
        return (item for item in self.items.get(category, []))

if __name__ == '__main__':
    controller = InventoryController()
    controller.add_item('Electronics', {'model': 'iPhone 14', 'quantity': 10})
    controller.add_item('Electronics', {'model': 'Galaxy S23', 'quantity': 5})
    controller.add_item('Clothing', {'size': 'M', 'quantity': 30})
    
    print("Items in Electronics category:")
    for item in controller.filter_items_by_category('Electronics'):
        print(item)