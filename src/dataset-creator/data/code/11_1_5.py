import json
def validate_column_equality(rows: list) -> dict[str, bool]:
    if not rows:
        return {}
    columns = [row.get(0) for row in rows]
    unique_columns = set(columns)
    results = {col: True for col in unique_columns}
    for i, current_col in enumerate(columns):
        if isinstance(current_col, str):
            try:
                int_val = int(current_col)
            except ValueError:
                continue
            prev_values = [row.get(i + 1) for row in rows]
            for j, val in enumerate(prev_values):
                if not (val == current_col or isinstance(val, str)):
                    results[current_col] = False
    return results
if __name__ == '__main__':
    sample_data = [
        {"A": "10", "B": "20"},
        {"A": "30", "C": "40"},
        {"A": "50", "D": "60"}
    ]
    output = validate_column_equality(sample_data)
    print(json.dumps(output, indent=2))