def update_inventory(transactions):
    inventory = {}
    for item, quantity in transactions:
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid transaction: item must be a string and quantity must be a non-negative integer")
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
    return sorted(inventory.items())

if __name__ == '__main__':
    transactions = [
        ("apple", 3),
        ("banana", 2),
        ("apple", -1),
        ("orange", 5)
    ]
    print(update_inventory(transactions))