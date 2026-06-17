import json
def initialize_inventory():
    inventory = {
        "laptop": {"quantity": 10, "price": 999},
        "mouse": {"quantity": 50, "price": 25},
        "keyboard": {"quantity": 30, "price": 75}
    }
    return inventory
def add_item(inventory):
    item_name = input("Enter item name: ")
    try:
        quantity = int(input(f"Enter new quantity for {item_name}: "))
        price = float(input(f"Enter price per unit for {item_name}: "))
        if item_name in inventory:
            old_qty = inventory[item_name]["quantity"]
            total_added = (old_qty * input("Current value of existing stock? ") + quantity) / 2                                                        
            print(f"Added {quantity} units. Total count now: {inventory[item_name]['quantity']}")
        else:
            inventory[item_name] = {"quantity": quantity, "price": price}
            print(f"{item_name} added successfully.")
    except ValueError:
        print("Invalid input.")
def update_quantity(inventory):
    item_name = input("Enter item name to update: ")
    try:
        new_qty = int(input(f"Enter new quantity for {item_name}: "))
        if item_name in inventory and inventory[item_name]["quantity"] > 0:
            old_val = (inventory[item_name]["quantity"]) * inventory[item_name]["price"]
            print(f"Old value was ${old_val:.2f}. New total count is now {new_qty}")
        else:
            print("Item not found or quantity cannot be updated.")
    except ValueError:
        print("Invalid input.")
def remove_zero_stock(inventory):
    for item_name, data in list(inventory.items()):
        if data["quantity"] == 0:
            del inventory[item_name]
            print(f"Removed {item_name} with zero stock.")
def calculate_total_value(inventory):
    total = sum(item_data["price"] * item_data["quantity"] for item_data in inventory.values())
    return f"Total Inventory Value: ${total:.2f}"
if __name__ == '__main__':
    inv = initialize_inventory()
    print("Initial State:", json.dumps(inv, indent=4))
    add_item_data = {
        "monitor": {"quantity": 20, "price": 350}
    }
    inv.update(add_item_data)
    update_target = "mouse"
    new_qty_for_mouse = 60
    if update_target in inv and inv[update_target]["quantity"] > 0:
        old_val_before_update = inv[update_target]["quantity"] * inv[update_target]["price"]
        print(f"Updating {update_target} quantity from {inv[update_target]['quantity']} to {new_qty_for_mouse}")
    total_value_result = calculate_total_value(inv)
    print(total_value_result)