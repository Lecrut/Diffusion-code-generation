import csv
import io

def calculate_average_weight(csv_data):
    reader = csv.reader(io.StringIO(csv_data))
    header = next(reader, None)
    if header is None:
        raise ValueError("CSV data is empty")

    weight_column_index = None
    for col_idx, col_name in enumerate(header):
        if col_name.strip().lower() == 'weight':
            weight_column_index = col_idx
            break

    if weight_column_index is None:
        raise ValueError("No 'weight' column found in CSV header")

    weights = []
    for row_num, row in enumerate(reader, start=2):
        if not row:
            continue
        if weight_column_index >= len(row):
            continue
        weight_str = row[weight_column_index].strip()
        if not weight_str:
            continue
        try:
            weight_value = float(weight_str)
            weights.append(weight_value)
        except ValueError:
            continue

    if not weights:
        raise ValueError("No valid weight values found")

    average_weight = sum(weights) / len(weights)
    return average_weight

if __name__ == '__main__':
    sample_csv = """name,weight,age
Alice,55.5,30
Bob,60.2,25
Charlie,invalid,35
Diana,70.0,28
Eve,58.3,32"""
    result = calculate_average_weight(sample_csv)
    print(result)