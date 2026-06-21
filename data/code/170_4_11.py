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
    controller.add_item({'name': 'apple', 'category': 'fruit'})
    controller.add_item({'name': 'banana', 'category': 'fruit'})
    controller.add_item({'name': 'carrot', 'category': 'vegetable'})

    fruit_items = controller.filter_by_category('fruit')
    for item in fruit_items:
        print(item)