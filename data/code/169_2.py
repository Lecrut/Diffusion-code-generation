def aggregate_inventory(item_counts):
    inventory = {}
    for item, count in item_counts:
        if item in inventory:
            inventory[item] += count
        else:
            inventory[item] = count
    return inventory
if __name__ == '__main__':
    sample_data = [
        ("Apple", 5),
        ("Banana", 10),
        ("Apple", 3),
        ("Orange", 7),
        ("Banana", 2)
    ]
    result = aggregate_inventory(sample_data)
    print(result)