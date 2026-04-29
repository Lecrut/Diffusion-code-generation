class CustomList:
    def __init__(self) -> None:
        self._items: list = []

    def add(self, item: int) -> None:
        self._items.append(item)

    def get_items(self) -> list:
        return self._items

if __name__ == '__main__':
    data_to_add = [10, 20, 30, 40, 50]
    custom_list = CustomList()
    count = 0
    for item in data_to_add:
        custom_list.add(item)
        count += 1
    
    result = custom_list.get_items()
    total = len(result)