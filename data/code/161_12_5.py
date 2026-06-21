class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name}: ${self.price:.2f}"

if __name__ == '__main__':
    items = [
        Item("Apple", 0.99),
        Item("Banana", 0.59),
        Item("Cherry", 1.49)
    ]
    
    for item in items:
        print(item.get_details())