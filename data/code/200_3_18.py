class DataFilter:
    def __init__(self, data):
        self.data = data

    def filter_keys(self, keys):
        return [{key: item[key] for key in keys if key in item} for item in self.data]

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    filter_keys = ['id', 'name']
    data_filter = DataFilter(sample_data)
    filtered_data = data_filter.filter_keys(filter_keys)
    print(filtered_data)