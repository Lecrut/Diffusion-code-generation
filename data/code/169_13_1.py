def calculate_inventory(counts):
    inventory = {}
    for item, count in enumerate(counts):
        try:
            if isinstance(count, (int, float)):
                inventory[f"item_{item}"] = int(count)
            else:
                inventory[f"item_{item}"] = 0
        except ValueError:
            inventory[f"item_{item}"] = 0
    return inventory
if __name__ == '__main__':
    sample_counts = [10, 5.5, "20", None, 3]
    result = calculate_inventory(sample_counts)
    print(result)