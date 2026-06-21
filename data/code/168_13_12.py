class StringCategorizer:
    def __init__(self):
        self.categories = {}

    def add_item(self, item):
        length = len(item)
        if length not in self.categories:
            self.categories[length] = []
        self.categories[length].append(item)

    def get_categories(self):
        return {key: sorted(value) for key, value in self.categories.items()}

if __name__ == '__main__':
    categorizer = StringCategorizer()
    items = ["apple", "banana", "carrot", "beef", "milk"]
    for item in items:
        categorizer.add_item(item)
    print(categorizer.get_categories())