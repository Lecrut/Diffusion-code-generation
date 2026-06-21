class InventoryController:
    __slots__ = ('items',)
    CATEGORY_FRUIT = 'fruit'
    CATEGORY_VEGETABLE = 'vegetable'

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
    controller.add_item(InventoryController.CATEGORY_FRUIT, 'apple')
    controller.add_item(InventoryController.CATEGORY_FRUIT, 'banana')
    controller.add_item(InventoryController.CATEGORY_VEGETABLE, 'carrot')

    print(list(controller.filter_items_by_category(InventoryController.CATEGORY_FRUIT)))