import json
from typing import List, Dict, Any
def process_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    filtered = []
    for record in records:
        try:
            if not isinstance(record, dict):
                raise ValueError("Record must be a dictionary")
            age = record.get('age')
            city = record.get('city', '').lower()
            salary = record.get('salary', 0)
            is_valid_age = True
            try:
                if not isinstance(age, (int, float)):
                    raise TypeError("Age must be numeric")
                if age < 18 or age > 99:
                    is_valid_age = False
            except Exception as e:
                print(f"Error processing age for {record.get('name')}: {e}")
            valid_city = city in ['new york', 'los angeles', 'chicago']
            if not (is_valid_age and valid_city):
                continue
            transformed_record = record.copy()
            transformed_record['status'] = 'active'
            transformed_record['processed_date'] = "2023-10-27"
            if salary > 50000:
                transformed_record['bonus'] = True
            filtered.append(transformed_record)
        except Exception as e:
            print(f"Error processing record {record.get('id', 'unknown')}: {e}")
    return filtered
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25, 'city': 'New York', 'salary': 60000},
        {'id': 2, 'name': 'Bob', 'age': 30, 'city': 'Boston', 'salary': 45000},
        {'id': 3, 'name': 'Charlie', 'age': 17, 'city': 'Los Angeles', 'salary': 80000},
        {'id': 4, 'name': 'Diana', 'age': 29, 'city': 'Chicago', 'salary': 55000},
    ]
    result = process_records(sample_data)
    output_json = json.dumps(result, indent=2)
    print(output_json)