import json

class Store:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._stores = {}

    def add_store(self, new_name: str, new_description: str) -> None:
        if not isinstance(new_name, str) or not isinstance(new_description, str):
            raise TypeError("Name and description must be strings.")
        self._stores[new_name] = new_description

    def get_store(self, name: str) -> str:
        return self._stores.get(name, "Store not found.")

    def export_to_json(self) -> str:
        return json.dumps({name: description for name, description in self._stores.items()}, indent=4)

if __name__ == '__main__':
    my_store_manager = Store("Tech Hub", "A place for all electronics.")
    my_store_manager.add_store("Electronics Corner", "All kinds of electronic gadgets and components.")
    my_store_manager.add_store("Book Nook", "A cozy spot for books and literature.")
    print(my_store_manager.get_store("Electronics Corner"))
    print(my_store_manager.export_to_json())