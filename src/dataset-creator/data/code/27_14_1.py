import collections as cd
class FruitClassifier:
    def __init__(self):
        self._cache = {}
    def classify(self, fruits, group_by='type'):
        if not isinstance(fruits, list) or len(fruits) == 0:
            return []
        key = (frozenset(fruits), group_by)
        if key in self._cache:
            return self._cache[key]
        classified = cd.defaultdict(list)
        for fruit in fruits:
            lower_fruit = str(fruit).lower()
            is_berry = any(b.lower() in lower_fruit for b in ['strawberry', 'blueberry', 'raspberry'])
            if group_by == 'type':
                categories = {
                    'citrus': {'orange', 'lemon', 'lime'},
                    'stone': {'peach', 'plum', 'apricot'},
                    'bushy': ['apple'],
                    'climbing': ['grape'],
                    'berry': [] if is_berry else [],
                }
            elif group_by == 'color':
                categories = {
                    'red': {'strawberry', 'blueberry', 'raspberry'},
                    'yellow': {'lemon', 'lime', 'peach'},
                    'green': ['apple'],
                    'purple': [],
                }
            elif group_by == 'texture':
                categories = {
                    'smooth': ['grape'],
                    'rough': ['strawberry', 'raspberry'],
                    'hard': {'orange', 'lemon'},
                    'soft': [] if is_berry else [],
                }
            else:
                classified[fruit] = f"Unknown group {group_by}"
            for cat_name, items in categories.items():
                if isinstance(items, list):
                    item_set = set(items)
                else:
                    item_set = items
                if lower_fruit in item_set or (is_berry and 'berry' == cat_name):
                    classified[cat_name].append(fruit)
        result_list = []
        for name, members in sorted(classified.items()):
            result_list.append((name, list(members)))
        self._cache[key] = result_list
        return result_list
if __name__ == '__main__':
    classifier = FruitClassifier()
    sample_fruits_1 = ['apple', 'orange', 'strawberry', 'grape']
    sample_fruits_2 = ['lemon', 'peach', 'blueberry']
    print(classifier.classify(sample_fruits_1, group_by='type'))
    print(classifier.classify(sample_fruits_2, group_by='color'))