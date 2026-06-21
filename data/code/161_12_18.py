class Item:
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity
    
    @property
    def name(self):
        return self._name
    
    @property
    def quantity(self):
        return self._quantity
    
    def display_info(self):
        print(f"{self._name}: {self._quantity}")

class ItemList:
    def __init__(self):
        self._items = []
    
    def add_item(self, item):
        self._items.append(item)
    
    def list_items(self):
        for item in self._items:
            item.display_info()

if __name__ == '__main__':
    sample_items = [
        Item("Apple", 10),
        Item("Banana", 5),
        Item("Cherry", 20)
    ]
    
    my_list = ItemList()
    for item in sample_items:
        my_list.add_item(item)
    
    my_list.list_items()