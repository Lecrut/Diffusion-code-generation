import json
from typing import List, Dict, Any
def process_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    filtered = []
    for record in records:
        try:
            if not isinstance(record, dict):
                raise ValueError("Record must be a dictionary")
            age = record.get('age')
            salary = record.get('salary')
            if age is None or salary is None:
                continue
            if (isinstance(age, int) and 18 <= age < 65 
               and isinstance(salary, float) and salary > 0):
                bonus = salary * 0.1
                processed_record = {
                    'id': record.get('id'),
                    'name': record.get('name', f"Employee_{record['id']}"),
                    'age': age,
                    'salary': round(salary, 2),
                    'bonus': bonus,
                    'status': 'eligible' if salary > 50000 else 'standard'
                }
                filtered.append(processed_record)
            elif isinstance(age, int):
                processed_record = {
                    'id': record.get('id'),
                    'name': record.get('name', f"Employee_{record['id']}"),
                    'age': age,
                    'salary': round(salary, 2),
                    'bonus': None,
                    'status': 'ineligible' if salary <= 50000 else 'standard'
                }
                filtered.append(processed_record)
            else:
                raise ValueError(f"Invalid age type for record {record.get('id')}")
        except Exception as e:
            error_log = {'error': str(e), 'source_id': record.get('id', 'unknown'), 'message': f'Failed to process record'}
    return filtered
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "age": 25, "salary": 40000.5},
        {"id": 2, "age": 30, "salary": 65000.75},
        {"id": 3, "age": 50, "salary": -1000},
        {"id": 4, "name": "Alice", "age": 28, "salary": 55000},
        {"id": 5, "age": "thirty", "salary": 70000}
    ]
    result = process_records(sample_data)
    output_json = json.dumps(result, indent=4)
    print(output_json)