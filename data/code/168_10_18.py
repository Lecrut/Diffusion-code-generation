from collections import defaultdict

class ItemCategorizer:
    DEFAULT_CATEGORY = "Uncategorized"

    @staticmethod
    def group_by_key(items, key):
        categories = defaultdict(list)
        for item in items:
            category = item.get(key, ItemCategorizer.DEFAULT_CATEGORY)
            categories[category].append(item)
        return dict(categories)

if __name__ == '__main__':
    sample_items = [
        {"type": "fruit", "name": "apple"},
        {"type": "fruit", "name": "banana"},
        {"type": "vegetable", "name": "carrot"},
        {"type": "fruit", "name": "orange"},
        {"type": "fruit", "name": "grape"},
        {"type": "vegetable", "name": "broccoli"},
        {"type": "fruit", "name": "kiwi"}
    ]
    categorized_items = ItemCategorizer.group_by_key(sample_items, "type")
    print(categorized_items)