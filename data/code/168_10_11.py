from collections import defaultdict

class ItemCategorizer:
    def __init__(self):
        self.categories = defaultdict(list)

    def add_item(self, item, category):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(item)

    def get_categories(self):
        return dict(self.categories)

if __name__ == '__main__':
    categorizer = ItemCategorizer()
    sample_items = ["apple", "banana", "carrot", "grape", "orange", "broccoli", "kiwi"]
    category_mapping = {
        "Fruits": ["apple", "banana", "grape", "orange"],
        "Vegetables": ["carrot", "broccoli", "kiwi"]
    }

    for item in sample_items:
        for category, values in category_mapping.items():
            if item in values:
                categorizer.add_item(item, category)
                break

    print(categorizer.get_categories())