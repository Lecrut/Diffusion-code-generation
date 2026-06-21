from typing import Dict

class StoreManager:
    def __init__(self):
        self._stores: Dict[str, int] = {
            "Store X": 10,
            "Store Y": 20,
            "Store Z": 30
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
        manager.add_store("Store Z", 35)
    except ValueError as e:
        print(e)
    print(manager.stores)