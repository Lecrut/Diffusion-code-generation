import json
from typing import List, Dict, Any
def process_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed = []
    for record in records:
        try:
            age = record.get('age')
            salary = record.get('salary')
            if not isinstance(age, (int, float)) or not isinstance(salary, (int, float)):
                raise ValueError("Invalid numeric type")
            is_eligible = False
            if age >= 18 and salary > 50000:
                is_eligible = True
            elif age < 25 and salary <= 30000:
                is_eligible = True
            else:
                raise ValueError("Record does not meet eligibility criteria")
            if is_eligible:
                transformed_record = {
                    'id': record.get('id'),
                    'name': record['name'],
                    'status': 'approved',
                    'bonus': salary * 0.1,
                    'risk_score': max(0, min(100, (50 - age) + (salary / 100))) if age < 25 else max(0, min(100, (30 - age) + (salary / 50)))
                }
            elif record.get('id'): 
                transformed_record = {
                    'id': record['id'],
                    'name': record['name'],
                    'status': 'rejected',
                    'bonus': 0,
                    'risk_score': None
                }
            processed.append(transformed_record)
        except Exception as e:
            error_record = {
                'error_code': 'VALIDATION_ERROR',
                'message': str(e),
                'original_data': record if isinstance(record, dict) else "Unknown"
            }
            processed.append(error_record)
    return processed
if __name__ == '__main__':
    sample_records = [
        {'id': 101, 'name': 'Alice', 'age': 25, 'salary': 60000},
        {'id': 102, 'name': 'Bob', 'age': 30, 'salary': 45000},
        {'id': 103, 'name': 'Charlie', 'age': 22, 'salary': 28000},
        {'id': 104, 'name': 'Diana', 'age': 65, 'salary': 70000}
    ]
    result = process_records(sample_records)
    output_json = json.dumps(result, indent=2)
    print(output_json)