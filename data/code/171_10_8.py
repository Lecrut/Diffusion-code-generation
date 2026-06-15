class Store:
    def __init__(self, name: str, description: str):
        self._name: str = name
        self._description: str = description
    def add_store(self, new_name: str, new_description: str) -> None:
        if not new_name or not new_description:
            raise ValueError("Store name and description cannot be empty.")
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
    another_store = Store("Book Nook", "Cozy bookstore with a wide selection of novels.")
    print(another_store.describe())
    try:
        my_store.add_store("New Name", "New Description")
        print(my_store.describe())
    except ValueError as e:
        print(f"Error: {e}")