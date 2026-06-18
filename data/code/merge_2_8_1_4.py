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
            department = record.get('department', '')
            if age is None or salary is None:
                continue
            try:
                int_age = int(age)
                float_salary = float(salary)
            except (ValueError, TypeError):
                raise ValueError(f"Invalid numeric data for {record}") from None
            if department == 'Engineering' and int_age > 25 and float_salary >= 80000:
                transformed_record = record.copy()
                transformed_record['status'] = 'eligible_for_bonus'
                transformed_record['adjusted_salary'] = round(float_salary * 1.1, 2)
                if not isinstance(transformed_record.get('id'), int):
                    raise ValueError("ID must be an integer")
                filtered.append(transformed_record)
            elif department == 'Sales':
                continue
        except Exception as e:
            print(f"Error processing record {record}: {e}")
    return filtered
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'age': 30, 'salary': 95000.50, 'department': 'Engineering'},
        {'id': 2, 'age': 45, 'salary': 75000.00, 'department': 'Sales'},
        {'id': 3, 'age': 28, 'salary': 120000.00, 'department': 'Engineering'},
        {'id': None, 'age': 35, 'salary': 90000.00, 'department': 'HR'},
        {'id': 4, 'age': 'thirty', 'salary': 85000.00, 'department': 'Engineering'},
    ]
    result = process_records(sample_data)
    output_json = json.dumps(result, indent=2)
    print(output_json)