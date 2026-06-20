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
        elif item.status == 'expired':
            result = f"{item.name} has expired"
        else:
            result = f"{item.name} status unknown"
        results.append(result)
    return results

if __name__ == '__main__':
    items = [
        Item("Item1", "active"),
        Item("Item2", "premium"),
        Item("Item3", "expired"),
        Item("Item4", "unknown")
    ]
    print(process_items(items))