class CustomList:
    """
    A custom list implementation allowing the addition of items.
    """
    def __init__(self):
        self._items = []

    def add(self, item: object) -> None:
        """
        Adds a single item to the end of the list.

        Args:
            item: The item to be added.
        """
        self._items.append(item)

    def get_items(self) -> list:
        """
        Returns the current list of items.

        Returns:
            list: The list of items.
        """
        return self._items

if __name__ == '__main__':
    data_list = CustomList()