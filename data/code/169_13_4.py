def calculate_inventory(item_counts):
    inventory = {}
    for count in item_counts:
        try:
            count_int = int(count)
            inventory[count] = inventory.get(count, 0) + count_int
        except (ValueError, TypeError):
            continue
    return inventory
if __name__ == '__main__':
    sample_counts = [10, 5.5, "20", "invalid", 3.5, 10]
    final_inventory = calculate_inventory(sample_counts)
    print(final_inventory)