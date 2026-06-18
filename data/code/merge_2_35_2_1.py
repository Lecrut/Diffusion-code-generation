def create_unique_item_store(items):
    return {item: True for item in set(items)}
class UniqueItemStoreError(Exception):
    pass
def find_value(store, key):
    if key not in store:
        raise UniqueItemStoreError(f"Key '{key}' does not exist.")
    return store[key]
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date']
    item_store = create_unique_item_store(sample_data)
    try:
        result = find_value(item_store, 'banana')
        print(f"Found value for banana")
    except UniqueItemStoreError as e:
        print(e)