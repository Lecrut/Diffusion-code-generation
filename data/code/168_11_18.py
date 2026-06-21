class StringCategorizer:
    def __init__(self):
        self.category_map = {}

    @staticmethod
    def _get_category_key(s):
        return s[0].lower()

    def categorize_strings(self, strings):
        for string in strings:
            category_key = self._get_category_key(string)
            if category_key not in self.category_map:
                self.category_map[category_key] = []
            self.category_map[category_key].append(string)

    def get_categorized_dict(self):
        return dict(sorted(self.category_map.items()))

if __name__ == '__main__':
    categorizer = StringCategorizer()
    sample_strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    categorizer.categorize_strings(sample_strings)
    print(categorizer.get_categorized_dict())