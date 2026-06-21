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

    def display(self):
        print(f"Item: {self.name}, Price: ${self.price:.2f}")

class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

if __name__ == '__main__':
    item1 = Item("Apple", 0.99)
    item2 = Item("Banana", 0.59)
    item3 = Item("Cherry", 2.49)

    my_list = ItemList()
    my_list.add_item(item1)
    my_list.add_item(item2)
    my_list.add_item(item3)

    my_list.items[0].display()
    print(f"Total Price: ${my_list.total_price():.2f}")