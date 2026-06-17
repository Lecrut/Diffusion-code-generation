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
            inventory[item_name] = max(0, new_qty)
            if inventory[item_name] == 0 and not any(i[1] > 0 for i in [(item_name, quantity) for item, quantity in inventory.items()]):
                del inventory[item_name]
    def remove_item(item_name):
        if item_name in inventory:
            old_qty = inventory[item_name]
            diff = -old_qty
            if not any(i[1] > 0 for i in [(item, quantity) for item, quantity in inventory.items()]):
                del inventory[item_name]
    def calculate_total_value():
        total = sum(inventory.get(item, 0) * prices.get(item, 0) for item in inventory.keys())
        return round(total, 2)
    add_item("mouse", 10)
    update_quantity("laptop", 45)
    remove_item("keyboard")
    print(f"Total Inventory Value: ${calculate_total_value():.2f}")
if __name__ == '__main__':
    main()