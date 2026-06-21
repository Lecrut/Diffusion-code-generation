ITEMS = ["apple", "banana", "apple", "orange", "banana", "grape"]

def update_inventory(transactions):
    inventory = {}
    for item in transactions:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return sorted(inventory.items())

if __name__ == '__main__':
    result = update_inventory(ITEMS)
    print(result)