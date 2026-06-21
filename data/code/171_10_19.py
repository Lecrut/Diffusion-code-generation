import json

class StoreManager:
    def __init__(self):
        self.stores = {}

    def add_store(self, name: str, description: str) -> None:
        if name in self.stores:
            raise ValueError(f"Store '{name}' already exists.")
        self.stores[name] = description

    def get_store(self, name: str) -> str:
        return self.stores.get(name, "Store not found.")

    def export_to_json(self) -> str:
        return json.dumps(self.stores, indent=4)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store("Tech Innovations", "A store for the latest tech gadgets.")
    manager.add_store("Bookworms", "Your one-stop shop for books and literature.")
    print(manager.get_store("Tech Innovations"))
    print(manager.export_to_json())