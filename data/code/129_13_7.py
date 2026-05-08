class ItemSorter:
    def sort_items(self, items, key, reverse=False):
        if not items:
            return []
        try:
            sorted_items = sorted(items, key=lambda item: item[key], reverse=reverse)
            return sorted_items
        except KeyError:
            raise ValueError(f"Key '{key}' not found in one of the item dictionaries.")
if __name__ == '__main__':
    sorter = ItemSorter()
    data = [
        {'name': 'Apple', 'price': 1.0, 'quantity': 100},
        {'name': 'Banana', 'price': 0.5, 'quantity': 200},
        {'name': 'Orange', 'price': 1.5, 'quantity': 50},
        {'name': 'Grape', 'price': 2.0, 'quantity': 150}
    ]
    print("Original Data:")
    for item in data:
        print(item)
    sorted_by_price = sorter.sort_items(data, 'price', reverse=False)
    print("\nSorted by Price (Ascending):")
    for item in sorted_by_price:
        print(item)
    sorted_by_quantity = sorter.sort_items(data, 'quantity', reverse=True)
    print("\nSorted by Quantity (Descending):")
    for item in sorted_by_quantity:
        print(item)
    sorted_by_name = sorter.sort_items(data, 'name', reverse=False)
    print("\nSorted by Name (Ascending):")
    for item in sorted_by_name:
        print(item)