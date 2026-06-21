class ItemList:
    DEFAULT_ITEMS = ["apple", "banana"]

    def __init__(self, initial_items=None):
        self.items = initial_items if initial_items is not None else self.DEFAULT_ITEMS.copy()

    @staticmethod
    def add_item(item_list, item):
        item_list.append(item)

    @staticmethod
    def remove_item(item_list, item):
        if item in item_list:
            item_list.remove(item)

    def list_items(self):
        return self.items

if __name__ == '__main__':
    my_list = ItemList()
    print("Initial items:", my_list.list_items())
    
    ItemList.add_item(my_list.items, 'cherry')
    print("After adding cherry:", my_list.list_items())
    
    ItemList.remove_item(my_list.items, 'apple')
    print("After removing apple:", my_list.list_items())