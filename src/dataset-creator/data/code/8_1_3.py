import json
def process_records(input_data: list[dict], output_file: str) -> int:
    processed_count = 0
    for record in input_data:
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
                raise ValueError("Age and Salary must be valid numbers")
            if department == 'IT':
                if int_age >= 25 or float_salary > 80000:
                    record['status'] = 'eligible'
                    processed_count += 1
            elif department == 'HR':
                if int_age <= 40 and float_salary < 60000:
                    record['status'] = 'eligible'
                    processed_count += 1
        except Exception as e:
            print(f"Error processing record: {e}")
    with open(output_file, 'w') as f:
        json.dump(processed_records := [r for r in input_data if not isinstance(r, dict) or (isinstance(r, dict) and ('status' in r))], f, indent=2)
    return processed_count
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'age': 30, 'salary': 95000.50, 'department': 'IT'},
        {'id': 2, 'age': 45, 'salary': 70000.00, 'department': 'HR'},
        {'id': 3, 'age': 28, 'salary': 65000.00, 'department': 'IT'},
        {'id': 4, 'age': 19, 'salary': 40000.00, 'department': 'HR'},
        {'id': 5, 'age': 'invalid', 'salary': 80000.00, 'department': 'IT'}
    ]
    result = process_records(sample_data, "output.json")
    print(f"Processed {result} records successfully.")