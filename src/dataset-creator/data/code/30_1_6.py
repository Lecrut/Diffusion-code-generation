import json
def categorize_records(records):
    categorized = {
        'names': [],
        'ages': []
    }
    for record in records:
        if isinstance(record.get('name'), str) and len(str(record['name'])) > 0:
            categorized['names'].append(record['name'])
        age_value = record.get('age')
        if isinstance(age_value, int):
            categorized['ages'].append(age_value)
    return categorized
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'name': 'Alice', 'age': 30},
        {'id': 102, 'name': 'Bob', 'age': 25},
        {'id': 103, 'name': '', 'age': None},
        {'id': 104, 'name': 'Charlie', 'age': 67}
    ]
    result = categorize_records(sample_data)
    print(json.dumps(result))