import csv
from typing import List, Dict, Any
def validate_column_equality(rows: List[List[Any]], columns_to_check: List[int]) -> bool:
    if not rows or not columns_to_check:
        return False
    num_rows = len(rows)
    for col_index in columns_to_check:
        if col_index < 0 or col_index >= max(len(row) for row in rows):
            continue
        column_values = [row[col_index] for row in rows]
        unique_vals = set(column_values)
        if len(unique_vals) > 1:
            return False
    return True
if __name__ == '__main__':
    sample_data = [
        ['Alice', '30', 'NYC'],
        ['Bob', '25', 'LA'],
        ['Charlie', '30', 'Chicago']                                                                                 
    ]
    columns_to_validate_indices = [1]                                                                        
    result = validate_column_equality(sample_data, columns_to_validate_indices)
    print(f"Validation Result: {result}")