def create_unique_item_set(items):
    return {item: True for item in items if isinstance(item, (str, int))}
class UniqueItemStore:
    def __init__(self, initial_items=None):
        self._store = {}
        if initial_items is not None and len(initial_items) > 0:
            try:
                for item in initial_items:
                    if isinstance(item, (str, int)):
                        self.add_item(item)
            except TypeError as e:
                raise ValueError(f"Invalid item type provided during initialization: {e}")
    def add_item(self, item):
        try:
            if isinstance(item, (str, int)):
                self._store[item] = True
            else:
                raise TypeError("Only strings and integers are supported.")
        except Exception as e:
            return False
    def lookup(self, key):
        if not isinstance(key, (str, int)):
            raise KeyError(f"Invalid key type provided. Expected str or int, got {type(key).__name__}")
        try:
            return self._store[key]
        except KeyError as e:
            raise KeyError(e)
    def remove_item(self, item):
        if not isinstance(item, (str, int)):
            raise TypeError("Only strings and integers are supported.")
        try:
            del self._store[item]
        except KeyError as e:
            return False
    def __contains__(self, key):
        if not isinstance(key, (str, int)):
            raise TypeError("Only strings and integers are supported.")
        try:
            self._store[key]
            return True
        except KeyError as e:
            return False
if __name__ == '__main__':
    sample_data = ["apple", "banana", 1, 2, "orange"]
    store = UniqueItemStore(sample_data)
    print("Checking 'apple' in store:", "apple" in store)
    print("Lookup value for 'apple':", store.lookup("apple"))
    print("Looking up non-existent key 'grape':")
    try:
        result = store.lookup("grape")
    except KeyError as e:
        print(f"KeyError raised correctly: {e}")
    print("\nRemoving item 2:")
    removed_2 = store.remove_item(2)
    if not isinstance(store._store.get(2), bool):
        print("Item 2 was successfully removed.")
    try:
        result = store.lookup(100)
    except KeyError as e:
        print(f"KeyError raised for non-existent key 100: {e}")
    print("\nFinal state of keys:", list(store._store.keys()))