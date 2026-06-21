def create_unique_item_list(item_objects):
    if not all(hasattr(obj, 'name') for obj in item_objects):
        raise ValueError("All items must have a 'name' attribute")
    
    return sorted({obj.name for obj in item_objects})

class Item:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    items = [Item(name) for name in ["banana", "apple", "cherry", "date", "elderberry"]]
    unique_items = create_unique_item_list(items)
    print(unique_items)