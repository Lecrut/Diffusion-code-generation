class ItemSorter:
    def __init__(self, categories):
        self.categories = categories
    def group_by_category(self, items):
        grouped = {category: [] for category in self.categories}
        for item in items:
            item_category = item.category
            if item_category in grouped:
                grouped[item_category].append(item)
        return grouped
class Item:
    def __init__(self, name, category):
        self.name = name
        self.category = category
if __name__ == '__main__':
    sample_items = [
        Item("Apple", "Fruit"),
        Item("Carrot", "Vegetable"),
        Item("Banana", "Fruit"),
        Item("Broccoli", "Vegetable"),
        Item("Orange", "Fruit"),
        Item("Potato", "Vegetable")
    ]
    defined_categories = ["Fruit", "Vegetable", "Dairy"]
    sorter = ItemSorter(defined_categories)
    result = sorter.group_by_category(sample_items)
    print(result)