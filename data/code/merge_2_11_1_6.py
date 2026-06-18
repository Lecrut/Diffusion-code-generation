import json
def validate_column_equality(rows: list) -> dict:
    if not isinstance(rows, list):
        raise TypeError("Input must be a list of dictionaries.")
    validation_results = {"status": "success", "errors": []}
    for row_idx, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        values_to_check = set()
        try:
            valid_columns = {col_name: col_value for col_name, col_value in row.items()}
            for key in list(valid_columns.keys()):
                value = str(valid_columns[key])
                if len(values_to_check) > 0 and not any(value == v for v in values_to_check):
                    validation_results["errors"].append(
                        f"Row {row_idx}: Inconsistent column '{key}' with other columns."
                    )
                values_to_check.add(value)
        except Exception:
            continue
    return validation_results
if __name__ == '__main__':
    sample_data = [
        {"id": "1", "value": "A"},
        {"id": "2", "value": "B"},
        {"id": "3", "value": "C"}
    ]
    result = validate_column_equality(sample_data)
    print(json.dumps(result, indent=4))