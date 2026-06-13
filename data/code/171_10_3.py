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
if __name__ == '__main__':
    my_store = Store("Tech Hub", "A place for all electronics.")
    print(my_store.describe())
    another_store = Store("Book Nook", "Cozy spot for reading and learning.")
    print(another_store.describe())
    my_store.add_store("New Location", "Updated details for the tech hub.")
    print(my_store.describe())