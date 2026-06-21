from typing import Dict

class StoreManager:
    def __init__(self):
        self._stores: Dict[str, int] = {
            "Store A": 5,
            "Store B": 3,
            "Store C": 8
        }

    @property
    def stores(self) -> Dict[str, int]:
        return self._stores

    def add_store(self, name: str, age: int):
        if name not in self._stores:
            self._stores[name] = age

if __name__ == '__main__':
    manager = StoreManager()
    print(manager.stores)
    manager.add_store("Store D", 2)
    print(manager.stores)