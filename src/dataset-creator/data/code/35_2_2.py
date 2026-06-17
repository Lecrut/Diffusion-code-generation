def create_unique_item_store(items):
    return {item: True for item in set(items)}
def find_value(unique_items_map, key):
    try:
        return unique_items_map[key]
    except KeyError:
        raise ValueError(f"Key '{key}' does not exist in the collection.")
if __name__ == '__main__':
    sample_data = [5, 10, 'apple', 3.14, 'banana']
    item_store = create_unique_item_store(sample_data)
    print("Available items:", list(item_store.keys()))
    test_keys = ['apple', 999]
    for k in test_keys:
        try:
            result = find_value(item_store, k)
            print(f"Found key {k}: {result}")
        except ValueError as e:
            print(e)