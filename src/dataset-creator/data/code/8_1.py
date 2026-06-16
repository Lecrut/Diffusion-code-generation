import json
def process_records(data):
    filtered = []
    for record in data:
        try:
            if not isinstance(record, dict) or 'id' not in record:
                raise ValueError("Invalid record structure")
            age = record.get('age', 0)
            salary = record.get('salary', 0)
            department = record.get('department')
            if age < 18 or salary <= 0:
                continue
            if 'bonus' in record and isinstance(record['bonus'], bool):
                transformed_record = {**record, 'status': 'eligible'}
                if not transformed_record['bonus']:
                    filtered.append(transformed_record)
        except Exception as e:
            print(f"Error processing record with ID {record.get('id')}: {e}")
    return filtered
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'age': 25, 'salary': 50000, 'department': 'IT', 'bonus': True},
        {'id': 2, 'age': 30, 'salary': -1000, 'department': 'HR'},
        {'id': 3, 'age': 45, 'salary': 80000, 'department': 'Finance', 'bonus': False},
        {'id': 4, 'age': 16, 'salary': 20000, 'department': 'Sales'},
    ]
    result = process_records(sample_data)
    output_json = json.dumps(result, indent=2)
    print(output_json)