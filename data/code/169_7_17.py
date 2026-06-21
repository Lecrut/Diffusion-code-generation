def update_inventory(transactions):
    inventory = {}
    for item, quantity in transactions:
        if quantity <= 0:
            continue
        inventory[item] = inventory.get(item, 0) + quantity
    return sorted(inventory.items())
if __name__ == '__main__':
    sample_transactions = [('apple', 3), ('banana', -1), ('orange', 2), ('apple', 5), ('pear', 4)]
    result = update_inventory(sample_transactions)
    print(result)