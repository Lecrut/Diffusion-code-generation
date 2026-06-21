class Item:
    def __init__(self, name, description):
        self._name = name
        self._description = description
    
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    def display_info(self):
        print(f"Item: {self._name}, Description: {self._description}")

class ItemList:
    def __init__(self):
        self._items = []
    
    def add_item(self, item):
        self._items.append(item)
    
    def list_items(self):
        for item in self._items:
            item.display_info()

if __name__ == '__main__':
    sample_data = [
        Item("Apple", "A fruit"),
        Item("Banana", "A yellow fruit"),
        Item("Cherry", "A small red fruit")
    ]
    
    my_list = ItemList()
    for item in sample_data:
        my_list.add_item(item)
    
    my_list.list_items()