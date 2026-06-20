class Item:
    def __init__(self, name, status):
        self.name = name
        self.status = status

def process_items(items):
    results = []
    for item in items:
        if item.status == 'active':
            result = f"{item.name} is active"
        elif item.status == 'premium':
            result = f"{item.name} is premium"
        else:
            result = f"{item.name} is expired"
        results.append(result)
    return results

if __name__ == '__main__':
    items = [
        Item("Item1", "active"),
        Item("Item2", "premium"),
        Item("Item3", "expired")
    ]
    print(process_items(items))