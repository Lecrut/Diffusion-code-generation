def calculate_inventory(counts):
    inventory = {}
    for count in counts:
        try:
            item_count = int(count)
            inventory[str(count)] = item_count
        except (ValueError, TypeError):
            inventory[str(count)] = None
    return inventory
if __name__ == '__main__':
    sample_counts = [10, "5", 22.5, "invalid", 100]
    final_inventory = calculate_inventory(sample_counts)
    print(final_inventory)