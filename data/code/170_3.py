class Inventory:
    def __init__(self, items):
        self.items = items
def print_inventory(inventory):
    print("--- Inventory List ---")
    for item in inventory.items:
        print(f"- {item}")
if __name__ == '__main__':
    sample_items = [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Webcam"
    ]
    my_inventory = Inventory(sample_items)
    print_inventory(my_inventory)