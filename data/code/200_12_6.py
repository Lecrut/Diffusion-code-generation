class DataProcessor:
    def __init__(self, data):
        self.data = data

    def extract_keys(self, keys):
        return list(map(lambda x: {k: x.get(k) for k in keys if k in x}, self.data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    keys_to_extract = ['id', 'name']
    processor = DataProcessor(sample_data)
    result = processor.extract_keys(keys_to_extract)
    print(result)