def find_max_inventory_store(inventory_data):
    if not inventory_data:
        return None, 0
    max_value = -float('inf')
    best_store_index = -1
    for i, store in enumerate(inventory_data):
        total_value = sum(store)
        if total_value > max_value:
            max_value = total_value
            best_store_index = i
    if best_store_index != -1:
        return inventory_data[best_store_index], max_value
    else:
        return None, 0
if __name__ == '__main__':
    sample_inventory = [
        [100, 50, 200],
        [300, 100, 50],
        [75, 25, 150]
    ]
    store, max_value = find_max_inventory_store(sample_inventory)
    print(f"Store with maximum total inventory value: {store}")
    print(f"Maximum total inventory value: {max_value}")