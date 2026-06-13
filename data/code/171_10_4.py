class Store:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description
    def add_store(self, new_name: str, new_description: str) -> None:
        if not new_name or not new_description:
            raise ValueError("Store name and description cannot be empty.")
        self.__name = new_name
        self.__description = new_description
    def get_store_name(self) -> str:
        return self.__name
    def get_store_description(self) -> str:
        return self.__description
    def describe(self) -> str:
        return f"Store Name: {self.__name}, Description: {self.__description}"
if __name__ == '__main__':
    my_store = Store("Tech Hub", "A place for all electronics and gadgets.")
    print(my_store.describe())
    another_store = Store("Book Nook", "Cozy bookstore with a wide selection of novels.")
    print(another_store.describe())
    try:
        my_store.add_store("New Name", "Updated description for the tech store.")
        print(my_store.describe())
    except ValueError as e:
        print(f"Error: {e}")