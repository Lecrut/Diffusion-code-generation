class Store:
    def __init__(self, name: str, description: str):
        self.__name: str = name
        self.__description: str = description
    def add_store(self, new_name: str, new_description: str) -> None:
        if not isinstance(new_name, str) or not isinstance(new_description, str):
            raise TypeError("Name and description must be strings.")
        self.__name = new_name
        self.__description = new_description
    def get_name(self) -> str:
        return self.__name
    def get_description(self) -> str:
        return self.__description
    def describe(self) -> str:
        return f"Store Name: {self.__name}, Description: {self.__description}"
if __name__ == '__main__':
    store1 = Store("Tech Hub", "A place for all electronics.")
    store2 = Store("Book Nook", "Cozy bookstore with rare editions.")
    print(store1.describe())
    print(f"Store 1 Name: {store1.get_name()}")
    print(f"Store 1 Description: {store1.get_description()}")
    print("-" * 20)
    print(store2.describe())
    print(f"Store 2 Name: {store2.get_name()}")
    print(f"Store 2 Description: {store2.get_description()}")
    store1.add_store("New Location", "Updated electronics section.")
    print("-" * 20)
    print(store1.describe())