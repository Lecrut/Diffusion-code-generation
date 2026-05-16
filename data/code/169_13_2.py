def calculate_inventory(counts):
    inventory = {}
    for count in counts:
        try:
            item_name = str(count)
            inventory[item_name] = int(count)
        except (ValueError, TypeError):
            continue
    return inventory
if __name__ == '__main__':
    sample_counts = [10, 5.5, "20", None, 3.14, 15]
    final_inventory = calculate_inventory(sample_counts)
    print(final_inventory)