def calculate_inventory(counts):
    inventory = {}
    for item, count in enumerate(counts):
        try:
            item_name = f"item_{item}"
            if isinstance(count, (int, float)):
                inventory[item_name] = int(count)
            else:
                inventory[item_name] = 0
        except Exception:
            inventory[f"item_{item}"] = 0
    return inventory
if __name__ == '__main__':
    sample_counts = [10, 5.5, "20", 3, None, 12.9]
    final_inventory = calculate_inventory(sample_counts)
    print(final_inventory)