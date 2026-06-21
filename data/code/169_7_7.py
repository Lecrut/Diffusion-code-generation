def update_inventory(transactions):
    inventory = {}
    for item, quantity in transactions:
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
    return sorted(inventory.items())

if __name__ == '__main__':
    transactions = [
        ('apple', 3),
        ('banana', 1),
        ('apple', -2),
        ('orange', 5)
    ]
    print(update_inventory(transactions))