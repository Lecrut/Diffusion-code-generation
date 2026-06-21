class Item:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def get_details(self):
        return f"{self._name}: ${self._price:.2f}"

class ItemList:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def list_items(self):
        for item in self._items:
            print(item.get_details())

if __name__ == '__main__':
    my_list = ItemList()
    my_list.add_item(Item("Apple", 0.99))
    my_list.add_item(Item("Banana", 0.59))
    my_list.list_items()