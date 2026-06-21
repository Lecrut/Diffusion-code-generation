from typing import Dict, Any
import json

class Store:
    def __init__(self, name: str, description: str):
        self._name: str = name
        self._description: str = description

    def add_store(self, new_name: str, new_description: str) -> None:
        if not isinstance(new_name, str) or not isinstance(new_description, str):
            raise TypeError("Name and description must be strings.")
        self._name = new_name
        self._description = new_description

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def describe(self) -> str:
        return f"Store Name: {self._name}, Description: {self._description}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self._name,
            "description": self._description
        }

def main():
    stores = {}
    store1 = Store("Tech Hub", "A place for all electronics.")
    stores["Tech Hub"] = store1.to_dict()
    
    store2 = Store("Bookworm", "A bookstore with a wide range of literature.")
    stores["Bookworm"] = store2.to_dict()
    
    json_data = json.dumps(stores, indent=4)
    print(json_data)

if __name__ == '__main__':
    main()