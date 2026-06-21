def extract_keys(data, keys):
    return list(map(lambda x: {k: x.get(k) for k in keys if k in x}, data))

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def extract_fields(self, fields):
        return extract_keys(self.data, fields)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    processor = DataProcessor(sample_data)
    fields_to_extract = ['id', 'name']
    result = processor.extract_fields(fields_to_extract)
    print(result)