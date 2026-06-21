class InventoryController:
    __slots__ = ('items',)
    
    def __init__(self):
        self.items = {}
    
    @classmethod
    def create_with_defaults(cls):
        controller = cls()
        controller.add_item('electronics', 'Laptop', 5)
        controller.add_item('accessories', 'Mouse', 20)
        controller.add_item('accessories', 'Keyboard', 15)
        return controller
    
    def add_item(self, category, name, quantity):
        if category not in self.items:
            self.items[category] = []
        self.items[category].append({'name': name, 'quantity': quantity})
    
    def filter_items_by_category(self, category):
        return (item for item in self.items.get(category, []))

if __name__ == '__main__':
    controller = InventoryController.create_with_defaults()
    print(list(controller.filter_items_by_category('accessories')))