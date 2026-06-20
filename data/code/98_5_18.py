class Item:
    def __init__(self, name, status):
        self.name = name
        self.status = status

def process_items(items):
    for item in items:
        if item.status == 'active':
            print(f"{item.name} is active.")
        elif item.status == 'premium':
            print(f"{item.name} is premium.")
        else:
            print(f"{item.name} is expired.")

if __name__ == '__main__':
    items = [
        Item("Item1", "active"),
        Item("Item2", "premium"),
        Item("Item3", "expired")
    ]
    process_items(items)