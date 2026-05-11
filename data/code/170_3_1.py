class Inventory:
    def __init__(self, items):
        self.items = items
def print_inventory(inventory):
    print("--- Inventory List ---")
    for item_name, quantity in inventory.items.items():
        print(f"Item: {item_name}, Quantity: {quantity}")
    print("----------------------")
if __name__ == '__main__':
    sample_items = {
        "Apples": 50,
        "Bananas": 120,
        "Oranges": 75,
        "Grapes": 30
    }
    my_inventory = Inventory(sample_items)
    print_inventory(my_inventory)