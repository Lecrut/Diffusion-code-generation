def filter_records(records):
    def passes(record):
        val = record.get('value', 0)
        cat = record.get('category', '')
        if val == 0:
            return True
        if val > 100 and cat == 'A':
            return True
        return False
    return [r for r in records if passes(r)]

if __name__ == '__main__':
    data = [
        {'value': 150, 'category': 'A'},
        {'value': 50, 'category': 'A'},
        {'value': 200, 'category': 'B'},
        {'value': 0, 'category': 'A'},
        {'value': 100, 'category': 'A'},
        {'value': 101, 'category': 'B'},
        {'value': 0, 'category': 'B'},
        {'value': 105, 'category': 'A'}
    ]
    result = filter_records(data)
    print(result)