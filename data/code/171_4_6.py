def find_max_inventory_store(inventory_data):
    if not inventory_data:
        return None, 0
    max_value = -float('inf')
    max_index = -1
    for i, data in enumerate(inventory_data):
        total_value = data['inventory'] * data['value']
        if total_value > max_value:
            max_value = total_value
            max_index = i
    if max_index != -1:
        return inventory_data[max_index], max_value
    else:
        return None, 0
if __name__ == '__main__':
    sample_data = [
        {'store_id': 'A', 'inventory': 100, 'value': 5},
        {'store_id': 'B', 'inventory': 200, 'value': 3},
        {'store_id': 'C', 'inventory': 50, 'value': 10},
        {'store_id': 'D', 'inventory': 300, 'value': 2},
    ]
    result_store, max_total_value = find_max_inventory_store(sample_data)
    print(f"Store with maximum total inventory value: {result_store}")
    print(f"Maximum total inventory value: {max_total_value}")