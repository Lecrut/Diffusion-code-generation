class InventoryController:
    __slots__ = ('items',)

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return (item for item in self.items if item['category'] == category)

if __name__ == '__main__':
    controller = InventoryController()
    controller.add_item({'name': 'Apple', 'category': 'Fruit'})
    controller.add_item({'name': 'Banana', 'category': 'Fruit'})
    controller.add_item({'name': 'Carrot', 'category': 'Vegetable'})

    for item in controller.filter_by_category('Fruit'):
        print(item)