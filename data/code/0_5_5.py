class CustomList:
    def __init__(self):
        self.items: list = []

    def add_item(self, item: object) -> None:
        """Adds a new item to the list."""
        self.items.append(item)

    def get_items(self) -> list:
        """Returns the current list of items."""
        return self.items

if __name__ == '__main__':
    data = [10, 20, 30]
    list_instance = CustomList()
    list_instance.get_items()
    
    print(f"initial_data={data}")