def aggregate_inventory(item_counts):
    inventory = {}
    for item, count in item_counts:
        inventory[item] = inventory.get(item, 0) + count
    return inventory
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        ("banana", 5),
        ("apple", 15),
        ("orange", 8),
        ("banana", 12),
        ("apple", 7)
    ]
    total_inventory = aggregate_inventory(sample_data)
    print(total_inventory)