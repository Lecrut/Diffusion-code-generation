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
    print("--- Initial Inventory ---")
    print(initial_inventory)
    print("\n--- Adding Items ---")
    add_item("Grapes", 200)
    add_item("Apples", 30)
    print("Inventory after additions:")
    print(get_count("Apples"))
    print(get_count("Grapes"))
    print("\n--- Updating Items ---")
    update_item("Bananas", 150)
    update_item("Oranges", 100)
    print("Inventory after updates:")
    print(get_count("Bananas"))
    print(get_count("Oranges"))
    print("\n--- Retrieving Counts ---")
    print("Final count for Apples:", get_count("Apples"))
    print("Final count for Bananas:", get_count("Bananas"))
    print("Final count for Pears (non-existent):", get_count("Pears"))