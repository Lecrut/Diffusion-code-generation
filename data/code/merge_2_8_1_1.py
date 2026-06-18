import json
def process_records(data):
    filtered = []
    for record in data:
        try:
            if not isinstance(record, dict) or 'id' not in record:
                raise ValueError("Invalid record structure")
            age = record.get('age')
            city = record.get('city')
            salary = record.get('salary', 0)
            if not (isinstance(age, int) and isinstance(city, str)):
                continue
            criteria_met = False
            if age >= 30:
                criteria_met = True
            elif 'tech' in city.lower():
                criteria_met = True
            if salary < 50000 or not criteria_met:
                raise ValueError("Record does not meet filtering criteria")
            transformed_record = {
                "id": record['id'],
                "status": "approved",
                "discount": int(salary * 0.1),
                "processed_at": "2023-10-27T10:00:00Z"
            }
            filtered.append(transformed_record)
        except Exception as e:
            print(f"Error processing record {record.get('id', 'unknown')}: {e}")
    return filtered
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "age": 35, "city": "New York", "salary": 60000},
        {"id": 2, "age": 28, "city": "Boston", "salary": 70000},
        {"id": 3, "age": 40, "city": "Seattle", "salary": 55000},
        {"id": 4, "age": 29, "city": "Tech Valley", "salary": 80000}
    ]
    result = process_records(sample_data)
    output_json = json.dumps(result, indent=2)
    print(output_json)