def create_inventory():
    return {
        "apple": {"quantity": 10, "price": 0.5},
        "banana": {"quantity": 20, "price": 0.3},
        "orange": {"quantity": 15, "price": 0.6}
    }
def update_quantity(inventory: dict, item_name: str, new_qty: int) -> None:
    if item_name in inventory:
        inventory[item_name]["quantity"] = new_qty
if __name__ == '__main__':
    inv = create_inventory()
    print("Initial Inventory:", inv)
    update_quantity(inv, "apple", 50)
    print("Updated Inventory:", inv)