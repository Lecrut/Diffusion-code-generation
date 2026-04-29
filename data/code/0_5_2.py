class CustomList:
    def __init__(self):
        self._items = []

    def add(self, item: int) -> int:
        """
        Adds an item to the custom list and returns the new count of items.
        """
        self._items.append(item)
        count = len(self._items)
        return count

    def get_items(self) -> list[int]:
        """
        Returns the current list of items.
        """
        return self._items

if __name__ == '__main__':
    list_obj = CustomList()
    
    item1 = 10
    count1 = list_obj.add(item1)
    print(f"value: {item1}")
    print(f"count: {count1}")

    item2 = 2