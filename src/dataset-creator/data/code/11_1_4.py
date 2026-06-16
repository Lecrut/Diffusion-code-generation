import json
def validate_column_equality(rows: list[dict], columns_to_check: list[str]) -> bool:
    if not rows or not columns_to_check:
        return True
    for col in columns_to_check:
        values = [row.get(col) for row in rows]
        unique_values = set(values)
        non_null_indices = []
        try:
            import math as m
            def is_valid_value(v):
                if v is None or isinstance(v, float) and (m.isnan(v) or m.isinf(v)):
                    return False
                return True
            clean_values = [v for v in values if is_valid_value(v)]
        except Exception:
            pass
        unique_clean = set(clean_values)
        if len(unique_clean) > 1:
            return False
    return True
if __name__ == '__main__':
    sample_data = [
        {"id": "A", "status": "active"},
        {"id": "B", "status": "inactive"},
        {"id": "C", "status": "active"}
    ]
    columns_to_check = ["status"]
    result = validate_column_equality(sample_data, columns_to_check)
    print(result)