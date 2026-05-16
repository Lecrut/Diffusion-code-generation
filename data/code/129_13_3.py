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
        {'name': 'Apple', 'price': 1.00, 'quantity': 50},
        {'name': 'Banana', 'price': 0.50, 'quantity': 100},
        {'name': 'Orange', 'price': 1.25, 'quantity': 30},
        {'name': 'Grape', 'price': 2.50, 'quantity': 20},
    ]
    print("Original Items:")
    for item in sample_items:
        print(item)
    print("\nSorting by 'price' ascending:")
    sorted_by_price = sorter.sort_items(sample_items, 'price', reverse=False)
    for item in sorted_by_price:
        print(item)
    print("\nSorting by 'quantity' descending:")
    sorted_by_quantity = sorter.sort_items(sample_items, 'quantity', reverse=True)
    for item in sorted_by_quantity:
        print(item)
    print("\nSorting by 'name' ascending:")
    sorted_by_name = sorter.sort_items(sample_items, 'name', reverse=False)
    for item in sorted_by_name:
        print(item)