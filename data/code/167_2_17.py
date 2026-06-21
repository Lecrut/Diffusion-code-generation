from typing import Dict

class StoreManager:
    def __init__(self):
        self.stores: Dict[str, int] = {
            "Store A": 5,
            "Store B": 3,
            "Store C": 7
        }

    @property
    def store_ages(self) -> Dict[str, int]:
        return self.stores

    def add_store(self, name: str, age: int):
        self.stores[name] = age

if __name__ == '__main__':
    manager = StoreManager()
    print(manager.store_ages)
    manager.add_store("Store D", 2)
    print(manager.store_ages)