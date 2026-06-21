from typing import Dict

class StoreManager:
    STORES: Dict[str, int] = {
        "Store Alpha": 10,
        "Store Beta": 15,
        "Store Gamma": 20
    }

    @property
    def stores(self) -> Dict[str, int]:
        return self.STORES

    def add_store(self, name: str, age: int):
        if name not in self.STORES:
            self.STORES[name] = age
        else:
            raise ValueError(f"Store {name} already exists.")

if __name__ == '__main__':
    manager = StoreManager()
    print(manager.stores)
    manager.add_store("Store Delta", 25)
    print(manager.stores)