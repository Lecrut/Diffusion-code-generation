class Item:
    def __init__(self, value, category):
        self.value = value
        self.category = category
class ItemSorter:
    def sort_items(self, items):
        sorted_items = sorted(items, key=lambda item: (item.category, item.value))
        return sorted_items
if __name__ == '__main__':
    items_list = [
        Item(5.5, "B"),
        Item(1.2, "A"),
        Item(8.0, "B"),
        Item(3.3, "A"),
        Item(9.1, "C")
    ]
    sorter = ItemSorter()
    sorted_list = sorter.sort_items(items_list)
    for item in sorted_list:
        print(f"Category: {item.category}, Value: {item.value}")