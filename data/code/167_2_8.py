from typing import List, Dict

class StoreManager:
    def __init__(self):
        self._stores: Dict[str, int] = {
            "Store A": 25,
            "Store B": 30,
            "Store C": 22
        }

    @property
    def stores(self) -> Dict[str, int]:
        return self._stores

    def add_store(self, name: str, age: int):
        if name not in self._stores:
            self._stores[name] = age
        else:
            raise ValueError(f"Store {name} already exists.")

if __name__ == '__main__':
    manager = StoreManager()
    print(manager.stores)
    try:
        manager.add_store("Store D", 28)
        print(manager.stores)
    except ValueError as e:
        print(e)