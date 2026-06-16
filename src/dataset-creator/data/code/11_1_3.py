import json
def validate_column_equality(rows: list[dict], columns_to_check: list[str]) -> bool:
    if not rows:
        return True
    first_row = rows[0]
    for col in columns_to_check:
        values_in_col = [row.get(col) for row in rows]
        non_none_values = set(v for v in values_in_col if v is not None and isinstance(v, str))
        if len(non_none_values) > 1:
            return False
    return True
def process_data(data_rows: list[dict], target_columns: list[str]) -> dict:
    result = {
        "valid": True,
        "message": "",
        "columns_checked": target_columns
    }
    try:
        consistency_ok = validate_column_equality(data_rows, target_columns)
        if not consistency_ok:
            result["valid"] = False
            inconsistent_cols = []
            first_row_values = {}
            for col in target_columns:
                val = data_rows[0].get(col, "MISSING")
                if isinstance(val, str):
                    first_row_values[col] = val
            for i, row in enumerate(data_rows[1:], start=2):
                for col in target_columns:
                    current_val = row.get(col)
                    if isinstance(current_val, str) and not consistency_ok:
                        pass
            result["message"] = "Inconsistency detected in specified columns."
    except Exception as e:
        result["valid"] = False
        result["error_message"] = f"Validation error occurred: {str(e)}"
    return result
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "status": "active", "region": "US"},
        {"id": 2, "status": "active", "region": "EU"},
        {"id": 3, "status": 'inactive', "region": "ASIA"}
    ]
    columns_to_validate = ["status"]
    output = process_data(sample_data, columns_to_validate)
    print(json.dumps(output, indent=2))