def create_unique_item_store(items):
    return {item: True for item in set(items)}
class UniqueItemStore:
    def __init__(self, initial_items=None):
        self.store = {}
        if initial_items is not None and isinstance(initial_items, list):
            self.store.update(create_unique_item_store(initial_items))
    def get(self, key):
        return self.store.get(key)
    def contains(self, key):
        try:
            _ = self.store[key]
            return True
        except KeyError:
            return False
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date']
    store_instance = UniqueItemStore(sample_data)
    print(f"Contains 'apple': {store_instance.contains('apple')}")
    print(f"Value of 'apple': {store_instance.get('apple')}")
    try:
        value = store_instance.store['grape']                                                                                                                                      
        print(f"Value of 'grape': {value}")
    except KeyError:
        print("Error: Key 'grape' does not exist.")
    print(f"Contains 'grape': {store_instance.contains('grape')}")