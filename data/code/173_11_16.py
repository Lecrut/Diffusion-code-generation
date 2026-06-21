from collections import defaultdict

class DataGrouper:
    DEFAULT_KEY = 'category'

    @staticmethod
    def group_data(data, key=DEFAULT_KEY):
        grouped = defaultdict(list)
        for item in data:
            grouped[item.get(key, '')].append(item)
        return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit'},
        {'id': 2, 'category': 'vegetable'},
        {'id': 3, 'category': 'fruit'},
        {'id': 4, 'category': 'meat'}
    ]
    grouped_data = DataGrouper.group_data(sample_data)
    print(grouped_data)