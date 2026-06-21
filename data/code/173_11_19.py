from collections import defaultdict

class DataGrouper:
    DEFAULT_KEY = 'category'

    @staticmethod
    def group_by_key(data, key=DEFAULT_KEY):
        grouped = defaultdict(list)
        for item in data:
            grouped[item.get(key, [])].append(item)
        return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit', 'name': 'apple'},
        {'id': 2, 'category': 'vegetable', 'name': 'carrot'},
        {'id': 3, 'category': 'fruit', 'name': 'banana'},
        {'id': 4, 'category': 'meat', 'name': 'chicken'}
    ]
    grouped_data = DataGrouper.group_by_key(sample_data)
    print(grouped_data)