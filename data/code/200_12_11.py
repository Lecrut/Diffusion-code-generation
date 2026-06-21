class DataProcessor:
    KEYS_TO_EXTRACT = ['name', 'age']

    @staticmethod
    def extract_keys(data):
        return list(map(lambda x: {k: x.get(k) for k in DataProcessor.KEYS_TO_EXTRACT if k in x}, data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    processor = DataProcessor()
    result = processor.extract_keys(sample_data)
    print(result)