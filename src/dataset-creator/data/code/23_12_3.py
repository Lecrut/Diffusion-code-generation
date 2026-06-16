def create_inventory():
    inventory = {
        "apple": {"quantity": 10, "price": 0.5},
        "banana": {"quantity": 20, "price": 0.3},
        "orange": {"quantity": 15, "price": 0.6}
    }
    return inventory
def update_quantity(inventory, item_name, new_qty):
    if item_name in inventory:
        inventory[item_name]["quantity"] = new_qty
        return True
    return False
if __name__ == '__main__':
    inv = create_inventory()
    print(f"Current apple quantity: {inv['apple']['quantity']}")
    update_quantity(inv, "banana", 30)
    print(f"Updated banana quantity to: {inv['banana']['quantity']}")