class InventoryController:
    __slots__ = ('items',)

    def __init__(self):
        self.items = []

    def add_item(self, item, category):
        self.items.append((item, category))

    def filter_by_category(self, category):
        return (item for item, cat in self.items if cat == category)

if __name__ == '__main__':
    controller = InventoryController()
    controller.add_item('apple', 'fruit')
    controller.add_item('banana', 'fruit')
    controller.add_item('carrot', 'vegetable')

    fruit_items = list(controller.filter_by_category('fruit'))
    print(fruit_items)