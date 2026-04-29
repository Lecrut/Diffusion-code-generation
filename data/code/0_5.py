class CustomList:
    """
    A custom list implementation allowing the addition of items.
    """
    def __init__(self) -> None:
        """
        Initializes an empty CustomList.
        """
        self._items: list = []

    def add(self, item: object) -> None:
        """
        Adds a specified item to the end of the list.

        Args:
            item: The item to be added to the list.
        """
        self._items.append(item)

    def get_items(self) -> list:
        """
        Returns the current list of items.

        Returns:
            The list of items.
        """
        return self._items

if __name__ == '__main__':
    data_list = CustomList()