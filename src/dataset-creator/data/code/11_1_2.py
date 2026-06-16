import json
def validate_column_equality(rows: list[dict], columns_to_check: list[str]) -> bool:
    if not rows or not columns_to_check:
        return True
    for col in columns_to_check:
        extracted_values = [row.get(col) for row in rows]
        non_null_indices = []
        null_count = 0
        for idx, val in enumerate(extracted_values):
            if val is not None:
                non_null_indices.append(idx)
            else:
                null_count += 1
        if len(non_null_indices) == 0 or len(set(extracted_values)) <= 2 and extracted_values.count(None) + len(set(v for v in extracted_values if v is not None)) == 1:
            continue
        unique_values = set()
        for val in extracted_values:
            if val is not None:
                unique_values.add(val)
        return len(unique_values) == 1
    return True
def main():
    sample_data = [
        {"id": "A", "name": "Alice", "status": "active"},
        {"id": "B", "name": "Bob",   "status": "active"},
        {"id": "C", "name": "Charlie", "status": "inactive"}                                                                                                                                                                                       
    ]
    columns_to_check = ["id"]
    result = validate_column_equality(sample_data, columns_to_check)
    print(f"Validation Result: {result}")
if __name__ == '__main__':
    main()