class DataFilterSorter:
    def __init__(self, data):
        self.data = data

    def filter_and_sort(self, key, value, sort_key='score', reverse=True):
        filtered = [item for item in self.data if item.get(key) == value]
        sorted_data = sorted(filtered, key=lambda x: x[sort_key], reverse=reverse)
        return sorted_data

if __name__ == '__main__':
    sample_data = [
        {'item': 'Apple', 'score': 85},
        {'item': 'Banana', 'score': 92},
        {'item': 'Cherry', 'score': 78},
        {'item': 'Date', 'score': 92},
        {'item': 'Elderberry', 'score': 88}
    ]
    sorter = DataFilterSorter(sample_data)
    result = sorter.filter_and_sort('item', 'Banana')
    print(result)