class Item:
    def __init__(self, value, category):
        self.value = value
        self.category = category
class ItemSorter:
    def sort_items(self, items):
        items.sort(key=lambda item: (item.category, item.value))
        return items
if __name__ == '__main__':
    items_list = [
        Item(5.5, "B"),
        Item(1.2, "A"),
        Item(8.0, "B"),
        Item(3.3, "A"),
        Item(1.2, "C")
    ]
    sorter = ItemSorter()
    sorted_items = sorter.sort_items(items_list)
    for item in sorted_items:
        print(f"Category: {item.category}, Value: {item.value}")