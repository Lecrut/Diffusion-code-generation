from typing import Dict

class StoreManager:
    STORE_AGE_MIN = 0

    def __init__(self):
        self._stores: Dict[str, int] = {'Store Alpha': 10, 'Store Beta': 15, 'Store Gamma': 20}

    @property
    def stores(self) -> Dict[str, int]:
        return self._stores

    def add_store(self, name: str, age: int):
        if name in self._stores:
            raise ValueError(f'Store {name} already exists.')
        elif age < self.STORE_AGE_MIN:
            raise ValueError(f'Store age must be at least {self.STORE_AGE_MIN}.')
        else:
            self._stores[name] = age
if __name__ == '__main__':
    manager = StoreManager()
    print(manager.stores)
    try:
        manager.add_store('Store Delta', 5)
        manager.add_store('Store Alpha', 10)
    except ValueError as e:
        print(e)