from typing import Dict

class StoreManager:
    def __init__(self):
        self._stores: Dict[str, int] = {
            "Store Alpha": 10,
            "Store Beta": 15,
            "Store Gamma": 20
        }
    
    @property
    def stores(self) -> Dict[str, int]:
        return self._stores
    
    def add_store(self, name: str, age: int):
        if name in self._stores:
            raise ValueError(f"Store {name} already exists.")
        self._stores[name] = age

if __name__ == '__main__':
    manager = StoreManager()
    print(manager.stores)
    try:
        manager.add_store("Store Delta", 25)
        print(manager.stores)
    except ValueError as e:
        print(e)