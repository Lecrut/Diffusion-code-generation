class RecordProcessor:
    def __init__(self, records):
        self.records = records
        self.threshold = 100
        self.target_category = 'A'

    def process(self):
        result = []
        for rec in self.records:
            val = rec.get('value', 0)
            cat = rec.get('category', '')
            if (val > self.threshold and cat == self.target_category) or (val == 0):
                result.append(rec)
        return result

if __name__ == '__main__':
    data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 101, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 101, 'category': 'A'}
    ]
    processor = RecordProcessor(data)
    print(processor.process())