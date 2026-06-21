def update_inventory(transactions):
    inventory = {}
    for item, quantity in transactions:
        if item not in inventory:
            inventory[item] = 0
        inventory[item] += quantity
    return sorted(inventory.items())

if __name__ == '__main__':
    sample_transactions = [
        ('apple', 3),
        ('banana', -1),
        ('apple', 2),
        ('orange', 5)
    ]
    print(update_inventory(sample_transactions))