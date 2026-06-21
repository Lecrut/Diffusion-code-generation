def update_inventory(transactions):
    inventory = {}
    for item, quantity in transactions:
        if quantity > 0:
            inventory[item] = inventory.get(item, 0) + quantity
    return sorted(inventory.items())

if __name__ == '__main__':
    transactions = [
        ('apple', 3),
        ('banana', 2),
        ('apple', -1),
        ('orange', 5)
    ]
    print(update_inventory(transactions))