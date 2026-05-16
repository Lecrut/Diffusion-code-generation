def manage_inventory(inventory):
    def add_item(item_name, quantity):
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity
    def update_item(item_name, new_quantity):
        if item_name in inventory:
            inventory[item_name] = new_quantity
        else:
            raise ValueError(f"Item '{item_name}' not found for update.")
    def get_count(item_name):
        return inventory.get(item_name, 0)
    return add_item, update_item, get_count
if __name__ == '__main__':
    initial_inventory = {
        "Apples": 50,
        "Bananas": 120,
        "Oranges": 75
    }
    add_item, update_item, get_count = manage_inventory(initial_inventory.copy())
    print("Initial Inventory:")
    print(initial_inventory)
    add_item("Grapes", 30)
    add_item("Apples", 15)
    print("\nInventory after additions:")
    print(get_count("Apples"))
    print(get_count("Grapes"))
    print(get_count("Bananas"))
    update_item("Oranges", 100)
    try:
        update_item("Pears", 50)
    except ValueError as e:
        print(f"\nError caught: {e}")
    print("\nFinal Inventory:")
    print(get_count("Apples"))
    print(get_count("Bananas"))
    print(get_count("Oranges"))
    print(get_count("Grapes"))
    print(get_count("Pears"))