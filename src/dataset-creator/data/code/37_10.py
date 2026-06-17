def main():
    inventory = {
        "laptop": 10,
        "mouse": 50,
        "keyboard": 25
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
        if item_name in inventory and new_qty >= 0:
            old_qty = inventory[item_name]
            diff = new_qty - old_qty
            for i in range(diff + 1):
                add_item(item_name, 1)
    def remove_zero_stock():
        to_remove = [item for item, qty in inventory.items() if qty == 0]
        for item in to_remove:
            del inventory[item]
    add_item("monitor", 15)
    update_quantity("mouse", 40)
    update_quantity("keyboard", 20)
    update_quantity("laptop", 8)
    remove_zero_stock()
    def calculate_total_value():
        total = sum(inventory[item] * prices.get(item, 0) for item in inventory)
        return round(total, 2)
    print(f"Total Inventory Value: ${calculate_total_value()}")
if __name__ == '__main__':
    main()