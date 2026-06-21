from typing import Dict

class StoreManager:
    def __init__(self):
        self._stores: Dict[str, int] = {
            "Store A": 5,
            "Store B": 3,
            "Store C": 7
        }

    @property
    def stores(self) -> Dict[str, int]:
        return self._stores

if __name__ == '__main__':
    manager = StoreManager()
    print(manager.stores)