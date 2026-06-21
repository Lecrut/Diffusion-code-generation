def create_unique_item_list(item_objects):
    item_names = {item.name for item in item_objects}
    return list(item_names)

if __name__ == '__main__':
    class Item:
        def __init__(self, name):
            self.name = name

    items = [
        Item("apple"),
        Item("banana"),
        Item("cherry"),
        Item("date"),
        Item("elderberry"),
        Item("apple")
    ]
    unique_items = create_unique_item_list(items)
    print(unique_items)