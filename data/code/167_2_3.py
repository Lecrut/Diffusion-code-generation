from typing import Dict

class StoreData:
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
        if name not in self._stores:
            self._stores[name] = age
        else:
            raise ValueError(f"Store {name} already exists.")

if __name__ == '__main__':
    store_manager = StoreData()
    print(store_manager.stores)
    store_manager.add_store("Store Delta", 25)
    print(store_manager.stores)