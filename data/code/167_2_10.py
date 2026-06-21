from typing import List, Tuple

class StoreManager:
    def __init__(self):
        self._stores: Dict[str, int] = {}

    @property
    def stores(self) -> Dict[str, int]:
        return self._stores.copy()

    def add_store(self, name: str, age: int):
        if not isinstance(name, str) or not isinstance(age, int):
            raise TypeError("Name must be a string and age must be an integer.")
        if name in self._stores:
            raise ValueError(f"Store {name} already exists.")
        self._stores[name] = age

    def display_stores(self):
        for name, age in sorted(self._stores.items()):
            print(f"Store: {name}, Age: {age}")

if __name__ == '__main__':
    manager = StoreManager()
    sample_stores = [("Store A", 25), ("Store B", 30), ("Store C", 22)]
    for name, age in sample_stores:
        manager.add_store(name, age)
    manager.display_stores()