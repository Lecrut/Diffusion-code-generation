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
    sample_data = [
        {'name': 'Apple', 'price': 1.50, 'quantity': 100},
        {'name': 'Banana', 'price': 0.75, 'quantity': 200},
        {'name': 'Orange', 'price': 1.25, 'quantity': 150},
        {'name': 'Grape', 'price': 3.00, 'quantity': 50},
    ]
    print("Original Data:")
    for item in sample_data:
        print(item)
    sorted_by_price = sorter.sort_items(sample_data, 'price', reverse=False)
    print("\nSorted by Price (Ascending):")
    for item in sorted_by_price:
        print(item)
    sorted_by_quantity = sorter.sort_items(sample_data, 'quantity', reverse=True)
    print("\nSorted by Quantity (Descending):")
    for item in sorted_by_quantity:
        print(item)
    sorted_by_name = sorter.sort_items(sample_data, 'name', reverse=False)
    print("\nSorted by Name (Ascending):")
    for item in sorted_by_name:
        print(item)