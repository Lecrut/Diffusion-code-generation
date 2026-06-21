class RecordFilter:
    def __init__(self):
        self.conditions = []

    def add_condition(self, name, func):
        self.conditions.append((name, func))

    def check_all(self, record):
        for name, func in self.conditions:
            if not func(record):
                return False
        return True

    def filter_records(self, records):
        return [record for record in records if self.check_all(record)]

def create_sample_filter():
    f = RecordFilter()
    f.add_condition('value_gt_10', lambda r: r.get('value', 0) > 10)
    f.add_condition('status_active', lambda r: r.get('status') == 'active')
    f.add_condition('date_valid', lambda r: isinstance(r.get('date'), str) and len(r['date'].split('-')) == 3)
    f.add_condition('id_positive', lambda r: isinstance(r.get('id'), int) and r['id'] > 0)
    f.add_condition('score_high', lambda r: r.get('score', 0) >= 50)
    return f

if __name__ == '__main__':
    sample_records = [
        {'id': 1, 'value': 15, 'status': 'active', 'date': '2023-01-15', 'score': 60},
        {'id': 2, 'value': 5, 'status': 'active', 'date': '2023-02-20', 'score': 70},
        {'id': 3, 'value': 20, 'status': 'inactive', 'date': '2023-03-10', 'score': 80},
        {'id': 4, 'value': 25, 'status': 'active', 'date': '2023-04-05', 'score': 40},
        {'id': 5, 'value': 30, 'status': 'active', 'date': '2023-05-25', 'score': 90},
    ]
    f = create_sample_filter()
    result = f.filter_records(sample_records)
    print(result)
    print(len(result))
    print(result[0]['id'] if result else None)