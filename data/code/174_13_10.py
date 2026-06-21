from collections import defaultdict

class DataGrouper:
    GROUP_KEY = 'category'

    @staticmethod
    def group_by_key(data_list):
        grouped_data = defaultdict(list)
        for item in data_list:
            key = item.get(DataGrouper.GROUP_KEY, None)
            if key is not None:
                grouped_data[key].append(item)
        return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'category': 'fruit', 'name': 'apple'},
        {'category': 'fruit', 'name': 'banana'},
        {'category': 'vegetable', 'name': 'carrot'},
        {'category': 'fruit', 'name': 'date'},
        {'category': 'grain', 'name': 'wheat'}
    ]
    grouped = DataGrouper.group_by_key(sample_data)
    print(grouped)