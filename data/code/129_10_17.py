class DataProcessor:
    def __init__(self):
        self.data = [
            {'item': 'Apple', 'score': 85},
            {'item': 'Banana', 'score': 92},
            {'item': 'Cherry', 'score': 78},
            {'item': 'Date', 'score': 92},
            {'item': 'Elderberry', 'score': 88}
        ]
    
    @staticmethod
    def filter_by_score(data, min_score):
        return [item for item in data if item['score'] >= min_score]
    
    @staticmethod
    def sort_data(data, key='score', reverse=True):
        return sorted(data, key=lambda item: item[key], reverse=reverse)
    
    def process_data(self, min_score):
        filtered = self.filter_by_score(self.data, min_score)
        sorted_data = self.sort_data(filtered)
        return sorted_data

if __name__ == '__main__':
    processor = DataProcessor()
    result = processor.process_data(80)
    for item in result:
        print(item)