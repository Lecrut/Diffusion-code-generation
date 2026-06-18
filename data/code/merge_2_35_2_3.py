def create_unique_item_store(items):
    return {item: True for item in set(items)}
def find_value(unique_items_dict, key):
    try:
        return unique_items_dict[key]
    except KeyError:
        raise ValueError(f"Key '{key}' does not exist in the collection.")
if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    item_store = create_unique_item_store(sample_data)
    test_keys = ["banana", "grape", "fig"]
    for key in test_keys:
        try:
            result = find_value(item_store, key)
            print(f"Found {key}: {result}")
        except ValueError as e:
            print(e)