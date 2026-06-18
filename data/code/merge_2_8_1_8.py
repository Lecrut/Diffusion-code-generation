import json
from typing import List, Dict, Any
def process_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed = []
    for record in records:
        try:
            if not isinstance(record, dict):
                raise ValueError("Record must be a dictionary")
            age = record.get('age')
            salary = record.get('salary')
            department = record.get('department', '')
            if age is None or salary is None:
                continue
            try:
                int_age = int(age)
                float_salary = float(salary)
            except (ValueError, TypeError):
                raise ValueError(f"Invalid numeric values for {record}")
            if department == 'Engineering' and int_age > 25:
                processed.append({**record, 'bonus': True})
            elif salary >= 100000:
                processed.append({**record, 'tier': 'Premium'})
            else:
                continue
        except Exception as e:
            print(f"Error processing record {record}: {e}")
            continue
    return processed
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'age': 30, 'salary': 85000.50, 'department': 'Engineering'},
        {'id': 2, 'age': 45, 'salary': 95000.75, 'department': 'Sales'},
        {'id': 3, 'age': 18, 'salary': 60000.00, 'department': 'Engineering'},
        {'id': 4, 'age': 28, 'salary': 'invalid', 'department': 'HR'},
    ]
    result = process_records(sample_data)
    output_json = json.dumps(result, indent=2)
    print(output_json)