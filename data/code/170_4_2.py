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
    controller.add_item('fruits', 'apple')
    controller.add_item('fruits', 'banana')
    controller.add_item('vegetables', 'carrot')

    print(list(controller.filter_items_by_category('fruits')))