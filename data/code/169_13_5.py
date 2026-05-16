def calculate_inventory(item_counts):
    inventory = {}
    for count in item_counts:
        try:
            item_value = int(count)
            inventory[item_value] = inventory.get(item_value, 0) + item_value
        except (ValueError, TypeError):
            pass
    return inventory
if __name__ == '__main__':
    sample_counts = [10, 5, "12", 3.5, "error", 10]
    final_inventory = calculate_inventory(sample_counts)
    print(final_inventory)