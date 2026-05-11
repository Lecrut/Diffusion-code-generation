if __name__ == '__main__':
    inventory_data = [
        ("apple", 10),
        ("banana", 5),
        ("apple", 15),
        ("orange", 8),
        ("banana", 12),
        ("apple", 7)
    ]
    inventory = {}
    for item_name, count in inventory_data:
        if item_name in inventory:
            inventory[item_name] += count
        else:
            inventory[item_name] = count
    print(inventory)