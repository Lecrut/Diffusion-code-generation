class DataFilter:
    def __init__(self, keys):
        self.keys = keys

    def filter_data(self, data_list):
        return [{key: item[key] for key in self.keys if key in item} for item in data_list]

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'id': 2, 'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
        {'id': 3, 'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
    ]
    
    filter_keys = ['id', 'name']
    data_filter = DataFilter(filter_keys)
    filtered_data = data_filter.filter_data(sample_data)
    
    for item in filtered_data:
        print(item)