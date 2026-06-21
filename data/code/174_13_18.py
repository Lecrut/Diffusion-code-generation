from collections import defaultdict

class GroupingDataStore:
    DEFAULT_KEY = 'group'

    @staticmethod
    def group_by_key(data, key=DEFAULT_KEY):
        grouped_data = defaultdict(list)
        for item in data:
            grouped_data[item.get(key, None)].append(item)
        return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'group': 'A', 'value': 10},
        {'id': 2, 'group': 'B', 'value': 20},
        {'id': 3, 'group': 'A', 'value': 30},
        {'id': 4, 'group': 'C', 'value': 40}
    ]
    grouped_result = GroupingDataStore.group_by_key(sample_data)
    print(grouped_result)