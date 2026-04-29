class CustomList:
    def __init__(self):
        self._items = []

    def add(self, item: object) -> None:
        """Adds an item to the custom list."""
        self._items.append(item)

    def get_items(self) -> list:
        """Returns the current list of items."""