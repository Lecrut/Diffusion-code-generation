from collections import defaultdict

class DictionaryGrouper:
    DEFAULT_KEY = 'category'

    @staticmethod
    def group_by_key(items, key=DEFAULT_KEY):
        groups = defaultdict(list)
        for item in items:
            category = item.get(key, None)
            if category is not None:
                groups[category].append(item)
            else:
                groups['uncategorized'].append(item)
        return dict(groups)

if __name__ == '__main__':
    sample_items = [
        {'id': 1, 'category': 'fruits'},
        {'id': 2, 'category': 'vegetables'},
        {'id': 3},
        {'id': 4, 'category': 'dairy'},
        {'id': 5}
    ]
    grouped_items = DictionaryGrouper.group_by_key(sample_items)
    print(grouped_items)