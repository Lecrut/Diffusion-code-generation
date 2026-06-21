def create_unique_item_names(item_objects):
    unique_names = set()
    for item in item_objects:
        unique_names.add(item.name)
    return list(unique_names)

if __name__ == '__main__':
    class Item:
        def __init__(self, name):
            self.name = name

    sample_items = [
        Item("apple"),
        Item("banana"),
        Item("cherry"),
        Item("date"),
        Item("elderberry"),
        Item("apple")
    ]
    
    unique_names = create_unique_item_names(sample_items)
    print(unique_names)