class DataProcessor:
    def __init__(self, data):
        self.data = data

    def extract_keys(self, key):
        return [item[key] for item in self.data if key in item]

if __name__ == '__main__':
    sample_data = [
        {'a': 1, 'b': 2},
        {'a': 3, 'c': 4},
        {'b': 5, 'd': 6}
    ]
    processor = DataProcessor(sample_data)
    a_values = processor.extract_keys('a')
    b_values = processor.extract_keys('b')
    print(a_values)
    print(b_values)