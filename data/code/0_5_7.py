class CustomList:
    MAX_CAPACITY = 10

    def __init__(self):
        self.items: list[int] = []

    def add(self, item: int) -> bool:
        """
        Adds an item to the custom list, checking against maximum capacity.

        Args:
            item: The integer value to be added.

        Returns:
            True if the item was successfully added, False otherwise.
        """
        if len(self.items) < self.MAX_CAPACITY:
            self.items.append(item)
            return True
        return False

    def get_items(self) -> list[int]:
        """
        Returns the current list of items.

        Returns:
            A list containing all items currently in the list.
        """
        return self.items

if __name__ == '__main__':
    list_instance = CustomList()
    item_one = 10
    item_two = 20
    item_three = 30
    item_four = 40
    item_five = 50
    item_six = 60