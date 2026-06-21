class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name}: ${self.price:.2f}"

if __name__ == '__main__':
    item1 = Item("Apple", 0.99)
    item2 = Item("Banana", 0.59)
    print(item1.get_details())
    print(item2.get_details())