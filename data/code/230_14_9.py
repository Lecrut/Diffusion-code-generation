class DataProcessor:
    def __init__(self, data):
        self.data = data

    def extract_ids(self):
        return list(map(lambda x: x['id'], self.data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]
    processor = DataProcessor(sample_data)
    ids = processor.extract_ids()
    print(ids)