def find_max_inventory_store(inventory_data):
    if not inventory_data:
        return None, 0
    max_value = -float('inf')
    best_store_index = -1
    for i, store_data in enumerate(inventory_data):
        total_value = sum(store_data.values())
        if total_value > max_value:
            max_value = total_value
            best_store_index = i
    if best_store_index != -1:
        return inventory_data[best_store_index], max_value
    else:
        return None, 0
if __name__ == '__main__':
    sample_inventory = [
        {'StoreA': 100, 'StoreB': 50},
        {'StoreA': 200, 'StoreB': 150},
        {'StoreA': 300, 'StoreB': 250}
    ]
    best_store, max_value = find_max_inventory_store(sample_inventory)
    print(f"Best Store Data: {best_store}")
    print(f"Maximum Total Inventory Value: {max_value}")