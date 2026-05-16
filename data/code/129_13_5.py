class ItemSorter:
    def sort_items(self, items, key, reverse=False):
        try:
            sorted_items = sorted(items, key=lambda item: item[key], reverse=reverse)
            return sorted_items
        except KeyError:
            raise ValueError(f"Key '{key}' not found in one of the item dictionaries.")
if __name__ == '__main__':
    sorter = ItemSorter()
    data = [
        {'name': 'Apple', 'price': 1.50, 'quantity': 100},
        {'name': 'Banana', 'price': 0.75, 'quantity': 250},
        {'name': 'Orange', 'price': 1.25, 'quantity': 150},
        {'name': 'Grape', 'price': 3.00, 'quantity': 50},
    ]
    print("Original Data:")
    for item in data:
        print(item)
    print("\nSorting by 'price' ascending:")
    sorted_by_price = sorter.sort_items(data, 'price', reverse=False)
    for item in sorted_by_price:
        print(item)
    print("\nSorting by 'quantity' descending:")
    sorted_by_quantity = sorter.sort_items(data, 'quantity', reverse=True)
    for item in sorted_by_quantity:
        print(item)
    print("\nSorting by 'name' ascending:")
    sorted_by_name = sorter.sort_items(data, 'name', reverse=False)
    for item in sorted_by_name:
        print(item)