class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_details(self):
        return f"{self.name}: {self.quantity}"

if __name__ == '__main__':
    item1 = Item("Apples", 10)
    item2 = Item("Oranges", 5)
    print(item1.get_details())
    print(item2.get_details())