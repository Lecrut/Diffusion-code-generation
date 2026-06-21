from typing import Dict

class StoreManager:
    def __init__(self) -> None:
        self._stores: Dict[str, int] = {
            "Store A": 5,
            "Store B": 10,
            "Store C": 3
        }

    @property
    def stores(self) -> Dict[str, int]:
        return self._stores

    def add_store(self, name: str, age: int) -> None:
        self._stores[name] = age

if __name__ == '__main__':
    manager = StoreManager()
    print(manager.stores)
    manager.add_store("Store D", 7)
    print(manager.stores)