CONDITIONS = [('value', '>', 10), ('status', '==', 'active'), ('date', '>=', '2023-01-01'), ('count', '<=', 50), ('score', '>=', 80)]

def filter_records(records):
    filtered = []
    for record in records:
        if all((record.get(key) and eval(f'record[key] {op} value') for key, op, value in CONDITIONS)):
            filtered.append(record)
    return filtered
if __name__ == '__main__':
    sample_records = [{'value': 15, 'status': 'active', 'date': '2023-02-01', 'count': 45, 'score': 85}, {'value': 9, 'status': 'inactive', 'date': '2023-01-15', 'count': 60, 'score': 75}, {'value': 20, 'status': 'active', 'date': '2023-03-01', 'count': 30, 'score': 90}]
    result = filter_records(sample_records)
    print(result)