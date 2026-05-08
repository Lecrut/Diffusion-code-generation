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
    sample_items = [
        {'name': 'Apple', 'price': 1.50, 'quantity': 100},
        {'name': 'Banana', 'price': 0.75, 'quantity': 250},
        {'name': 'Orange', 'price': 1.25, 'quantity': 150},
        {'name': 'Grapes', 'price': 5.00, 'quantity': 50},
    ]
    print("Original Items:")
    for item in sample_items:
        print(item)
    sorted_by_price = sorter.sort_items(sample_items, 'price', reverse=False)
    print("\nSorted by Price (Ascending):")
    for item in sorted_by_price:
        print(item)
    sorted_by_quantity = sorter.sort_items(sample_items, 'quantity', reverse=True)
    print("\nSorted by Quantity (Descending):")
    for item in sorted_by_quantity:
        print(item)
    sorted_by_name = sorter.sort_items(sample_items, 'name', reverse=False)
    print("\nSorted by Name (Ascending):")
    for item in sorted_by_name:
        print(item)