from collections import defaultdict

class GroupingHelper:
    DEFAULT_KEY = 'category'

    @staticmethod
    def group_by_key(data, key=DEFAULT_KEY):
        grouped_data = defaultdict(list)
        for item in data:
            grouped_data[item.get(key, [])].append(item)
        return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'category': 'fruit', 'name': 'apple'},
        {'category': 'vegetable', 'name': 'carrot'},
        {'category': 'fruit', 'name': 'banana'},
        {'category': 'meat', 'name': 'chicken'}
    ]
    
    grouped_data = GroupingHelper.group_by_key(sample_data)
    print(grouped_data)