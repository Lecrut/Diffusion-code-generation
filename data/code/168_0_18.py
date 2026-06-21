from collections import defaultdict

class DictGrouper:
    DEFAULT_KEY = 'category'

    @staticmethod
    def group_by_key(items, key=DEFAULT_KEY):
        grouped_items = defaultdict(list)
        for item in items:
            category = item.get(key, 'uncategorized')
            grouped_items[category].append(item)
        return dict(grouped_items)

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'category': 'fruits'},
        {'name': 'banana', 'category': 'fruits'},
        {'name': 'carrot', 'category': 'vegetables'},
        {'name': 'broccoli', 'category': 'vegetables'},
        {'name': 'milk', 'category': 'dairy'},
        {'name': 'cheese', 'category': 'dairy'}
    ]
    grouped_items = DictGrouper.group_by_key(sample_items)
    print(grouped_items)