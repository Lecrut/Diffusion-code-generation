class StringCategorizer:
    def __init__(self):
        self.categories = {}

    def add_category(self, length, item):
        if length not in self.categories:
            self.categories[length] = []
        self.categories[length].append(item)

    def categorize_strings(self, string_list):
        for item in string_list:
            length = len(item)
            self.add_category(length, item)

    def get_categories(self):
        return {k: sorted(v) for k, v in self.categories.items()}

if __name__ == '__main__':
    categorizer = StringCategorizer()
    sample_strings = ["apple", "banana", "cherry", "date", "elderberry"]
    categorizer.categorize_strings(sample_strings)
    print(categorizer.get_categories())