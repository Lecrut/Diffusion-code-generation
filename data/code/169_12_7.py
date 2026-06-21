from collections import Counter

ITEM_COUNTS = [
    ("apple", 10),
    ("banana", 5),
    ("apple", 15),
    ("orange", 8),
    ("banana", 12),
    ("apple", 7)
]

def aggregate_inventory(item_counts):
    inventory = {}
    for item, count in item_counts:
        inventory[item] = inventory.get(item, 0) + count
    return inventory

if __name__ == '__main__':
    total_inventory = aggregate_inventory(ITEM_COUNTS)
    print(total_inventory)