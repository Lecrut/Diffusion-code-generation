class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def sort_items(items, attribute='value'):
    return sorted(items, key=lambda item: getattr(item, attribute))

if __name__ == '__main__':
    items = [
        Item("Apple", 10),
        Item("Banana", 5),
        Item("Cherry", 20)
    ]
    sorted_items = sort_items(items)
    for item in sorted_items:
        print(f"{item.name}: {item.value}")