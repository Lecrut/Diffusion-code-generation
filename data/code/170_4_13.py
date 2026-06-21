class InventoryController:
    __slots__ = ('items',)
    
    def __init__(self):
        self.items = {}
    
    def add_item(self, category, item_name, quantity):
        if category not in self.items:
            self.items[category] = []
        self.items[category].append({'name': item_name, 'quantity': quantity})
    
    def filter_items_by_category(self, category):
        return (item for item in self.items.get(category, []))

if __name__ == '__main__':
    controller = InventoryController()
    controller.add_item('electronics', 'Laptop', 5)
    controller.add_item('electronics', 'Mouse', 20)
    controller.add_item('accessories', 'Keyboard', 15)
    
    print("Items in electronics category:")
    for item in controller.filter_items_by_category('electronics'):
        print(item)
    
    print("\nItems in accessories category:")
    for item in controller.filter_items_by_category('accessories'):
        print(item)