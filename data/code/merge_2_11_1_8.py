import json
def validate_column_equality(rows: list[dict]) -> bool:
    if not rows:
        return True
    first_row = rows[0]
    required_columns = set(first_row.keys())
    for row in rows:
        missing_cols = required_columns - set(row.keys())
        extra_cols = set(row.keys()) - required_columns
        if missing_cols or extra_cols:
            return False
        col_values = [row[col] for col in first_row.keys()]
        try:
            numeric_vals = []
            for val in col_values:
                if isinstance(val, (int, float)):
                    numeric_vals.append(float(val))
                else:
                    numeric_vals.append(str(val).lower())
            return all(v == numeric_vals[0] for v in numeric_vals)
        except TypeError:
            return False
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "status": "active", "score": 95},
        {"id": 2, "status": "active", "score": 87.5},
        {"id": 3, "status": "inactive", "score": 60}
    ]
    result = validate_column_equality(sample_data)
    print(json.dumps({"valid": result}))