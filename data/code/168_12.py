class ItemSorter:
    def __init__(self, categories):
        self.categories = categories
    def group_by_category(self, items):
        grouped = {category: [] for category in self.categories}
        for item in items:
            item_category = None
            for category in self.categories:
                if hasattr(item, 'category') and item.category == category:
                    item_category = category
                    break
            if item_category:
                grouped[item_category].append(item)
            else:
                pass
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
        Item("Potato", "Vegetable"),
        Item("Grape", "Fruit")
    ]
    defined_categories = ["Fruit", "Vegetable", "Dairy"]
    sorter = ItemSorter(defined_categories)
    result = sorter.group_by_category(sample_items)
    for category, items in result.items():
        print(f"--- {category} ---")
        for item in items:
            print(f"{item.name}")
        print()