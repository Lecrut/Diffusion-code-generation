class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_details(self):
        return f"Item ID: {self.id}, Name: {self.name}, Price: ${self.price:.2f}"

def create_items():
    items = [
        Item(1, "Apple", 0.99),
        Item(2, "Banana", 0.59),
        Item(3, "Cherry", 2.49)
    ]
    return items

if __name__ == '__main__':
    items = create_items()
    for item in items:
        print(item.get_details())