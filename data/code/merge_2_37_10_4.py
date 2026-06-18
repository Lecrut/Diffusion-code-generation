def main():
    inventory = {
        "laptop": 50,
        "mouse": 120,
        "keyboard": 80
    }
    prices = {
        "laptop": 999.99,
        "mouse": 29.99,
        "keyboard": 79.99
    }
    def add_item(item_name, quantity):
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity
    def update_quantity(item_name, new_qty):
        if item_name in inventory:
            old_qty = inventory[item_name]
            diff = new_qty - old_qty
            add_item(item_name, diff)
    def remove_zero_stock():
        items_to_remove = [item for item, qty in inventory.items() if qty <= 0]
        for item in items_to_remove:
            del inventory[item]
    def calculate_total_value():
        total = sum(inventory.get(item, 0) * prices.get(item, 0) for item in inventory.keys())
        return round(total, 2)
    add_item("mouse", 15)
    update_quantity("laptop", 40)
    remove_zero_stock()
    print(f"Total Inventory Value: ${calculate_total_value():.2f}")
if __name__ == '__main__':
    main()