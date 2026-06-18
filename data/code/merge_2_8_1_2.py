import json
def process_records(input_data: list[dict], min_age: int = 18) -> dict[str, any]:
    filtered_results = []
    for record in input_data:
        try:
            if not isinstance(record.get('age'), (int, float)):
                raise ValueError("Invalid age type")
            if record['age'] >= min_age and 'status' == 'active':
                transformed_record = {
                    "id": record["id"],
                    "name": f"{record['first_name']} {record['last_name']}",
                    "eligible_status": True,
                    "score": round(record.get('performance_score', 0) * 1.5, 2),
                }
                if transformed_record["score"] > record.get("threshold", 90):
                    filtered_results.append(transformed_record)
        except (ValueError, KeyError) as e:
            print(f"Processing error for ID {record.get('id')}: {e}")
    return {"total_processed": len(filtered_results), "records": filtered_results}
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "first_name": "Alice", "last_name": "Smith", "age": 25, "status": "active", "performance_score": 85},
        {"id": 2, "first_name": "Bob", "last_name": "Jones", "age": 30, "status": "inactive", "performance_score": 92},
        {"id": 3, "first_name": "Charlie", "last_name": "Brown", "age": 17, "status": "active", "performance_score": 88},
        {"id": 4, "first_name": "Diana", "last_name": "Ross", "age": 29, "status": "active", "performance_score": 95},
    ]
    result = process_records(sample_data)
    output_json = json.dumps(result, indent=2)
    print(output_json)