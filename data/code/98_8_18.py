class RecordFilter:
    def __init__(self, threshold=100, target_category='A', special_value=0):
        self.threshold = threshold
        self.target_category = target_category
        self.special_value = special_value

    def should_keep(self, record):
        value = record.get('value')
        category = record.get('category')
        if value is None or category is None:
            return False
        is_high_category = value > self.threshold and category == self.target_category
        is_special = value == self.special_value
        return is_high_category or is_special

    def filter_records(self, records):
        return [r for r in records if self.should_keep(r)]

if __name__ == '__main__':
    data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 101, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 101, 'category': 'A'},
        {'value': 100, 'category': 'B'},
        {'value': -10, 'category': 'A'}
    ]
    processor = RecordFilter()
    result = processor.filter_records(data)
    print(result)
    print(len(result))
    print(processor.should_keep({'value': 101, 'category': 'A'}))
    print(processor.should_keep({'value': 0, 'category': 'B'}))
    print(processor.should_keep({'value': 100, 'category': 'A'}))