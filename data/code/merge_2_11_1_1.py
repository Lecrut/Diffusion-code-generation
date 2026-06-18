import json
def validate_column_equality(rows: list[list], column_indices: list[int]) -> bool:
    if not rows or not column_indices:
        return True
    for idx in set(column_indices):
        values = [row[idx] for row in rows]
        unique_values = set(values)
        if len(unique_values) > 1:
            return False
    return True
def process_data(data_rows: list[list], target_columns: list[int]) -> dict[str, bool]:
    results = {}
    for col_idx in target_columns:
        is_valid = validate_column_equality(data_rows, [col_idx])
        results[f"column_{col_idx}"] = is_valid
    return results
if __name__ == '__main__':
    sample_data = [
        ["Alice", 30, "NYC"],
        ["Bob", 25, "LA"],
        ["Charlie", 40, "Chicago"]
    ]
    columns_to_check = [1]
    validation_results = process_data(sample_data, columns_to_check)
    print(json.dumps(validation_results))