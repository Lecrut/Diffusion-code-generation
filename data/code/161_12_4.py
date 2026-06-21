class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def display(self):
        return f"{self.name}: {self.quantity}"

if __name__ == '__main__':
    item1 = Item("Apples", 3)
    item2 = Item("Bananas", 5)
    print(item1.display())
    print(item2.display())