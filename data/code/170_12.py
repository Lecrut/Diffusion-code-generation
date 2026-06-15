import csv
class Inventory:
    def __init__(self):
        self.items = {}
def load_inventory_from_csv(filename, inventory):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header is None:
                return True
            for row in reader:
                if len(row) == 2:
                    item_id = row[0].strip()
                    quantity = row[1].strip()
                    if item_id and quantity.isdigit():
                        inventory.items[item_id] = int(quantity)
                    else:
                        print(f"Skipping invalid row: {row}")
                else:
                    print(f"Skipping malformed row: {row}")
        return True
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return False
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return False
if __name__ == '__main__':
    inventory_data = [
        ["Item ID", "Quantity"],
        ["A101", "50"],
        ["B202", "120"],
        ["C303", "75"],
        ["D404", "invalid"]
    ]
    filename = "inventory_sample.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(inventory_data)
    my_inventory = Inventory()
    print("Attempting to load inventory from CSV...")
    success = load_inventory_from_csv(filename, my_inventory)
    if success:
        print("\nInventory loaded successfully:")
        print(my_inventory.items)
    else:
        print("\nInventory loading failed.")