from typing import Any
class UniqueItemStore:
    def __init__(self):
        self._items = {}
    def add(self, key: str, value: Any) -> None:
        if key in self._items:
            raise ValueError(f"Key '{key}' already exists.")
        self._items[key] = value
    def get(self, key: str) -> Any:
        return self._items.get(key)
if __name__ == '__main__':
    store = UniqueItemStore()
    sample_values = [
        ("apple", "fruit"),
        ("banana", "food"),
        ("carrot", "vegetable")
    ]
    for key, value in sample_values:
        try:
            store.add(key, value)
        except ValueError as e:
            print(f"Error adding {key}: {e}")
    test_keys = ["apple", "banana", "nonexistent"]
    for k in test_keys:
        result = store.get(k)
        if result is not None:
            print(f"Key '{k}' -> Value: {result}")
        else:
            try:
                _ = store._items[k]                                                                
                print("Internal error detected")
            except KeyError:
                pass
    if k == "nonexistent":
        print(f"Key '{k}' not found.")
    try:
        store.add("apple", "new_fruit_type")
    except ValueError as e:
        print(e)