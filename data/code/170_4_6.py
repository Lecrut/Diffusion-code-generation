class InventoryController:
    __slots__ = ('items',)
    categories = {'Electronics', 'Peripherals'}

    def __init__(self):
        self.items = {category: [] for category in self.categories}

    @staticmethod
    def validate_category(category):
        if category not in InventoryController.categories:
            raise ValueError(f"Invalid category: {category}")

    def add_item(self, category, name, quantity):
        self.validate_category(category)
        item = {"name": name, "quantity": quantity}
        self.items[category].append(item)

    def filter_items_by_category(self, category):
        self.validate_category(category)
        return (item for item in self.items.get(category, []))

if __name__ == '__main__':
    controller = InventoryController()
    controller.add_item('Electronics', 'Laptop', 5)
    controller.add_item('Peripherals', 'Mouse', 20)
    controller.add_item('Peripherals', 'Keyboard', 15)

    print("Electronics inventory:")
    for item in controller.filter_items_by_category('Electronics'):
        print(item)

    print("\nPeripherals inventory:")
    for item in controller.filter_items_by_category('Peripherals'):
        print(item)

    try:
        controller.add_item('Audio', 'Headphones', 10)
    except ValueError as e:
        print(e)