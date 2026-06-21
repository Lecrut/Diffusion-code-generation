from typing import List

class StoreManager:
    def __init__(self):
        self._stores: List[str] = [
            "Store A",
            "Store B",
            "Store C"
        ]
        self._ages: List[int] = [
            25,
            30,
            22
        ]

    @property
    def stores(self) -> List[str]:
        return self._stores

    @property
    def ages(self) -> List[int]:
        return self._ages

    def add_store(self, name: str, age: int):
        if name not in self._stores:
            self._stores.append(name)
            self._ages.append(age)
        else:
            raise ValueError(f"Store {name} already exists.")

if __name__ == '__main__':
    manager = StoreManager()
    print("Initial stores:", manager.stores)
    print("Initial ages:", manager.ages)
    try:
        manager.add_store("Store D", 2)
        print("Added new store:", "Store D")
        print("Updated stores:", manager.stores)
        print("Updated ages:", manager.ages)
    except ValueError as e:
        print(e)