class InventoryController:
    __slots__ = ('items',)

    def __init__(self):
        self.items = {}

    @staticmethod
    def _category_key(category):
        return f"category_{category}"

    def add_item(self, category, item_id, name, quantity):
        if category not in self.items:
            self.items[InventoryController._category_key(category)] = []
        self.items[InventoryController._category_key(category)].append({'id': item_id, 'name': name, 'quantity': quantity})

    def filter_items_by_category(self, category):
        key = InventoryController._category_key(category)
        return (item for item in self.items.get(key, []))

if __name__ == '__main__':
    controller = InventoryController()
    controller.add_item('electronics', 101, "Laptop", 5)
    controller.add_item('electronics', 102, "Mouse", 20)
    controller.add_item('electronics', 103, "Keyboard", 15)
    print(list(controller.filter_items_by_category('electronics')))