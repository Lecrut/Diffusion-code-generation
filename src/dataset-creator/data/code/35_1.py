import csv
from pathlib import Path
def load_numeric_data(file_paths: list[str], column_name: str) -> dict[int, float]:
    result = {}
    sorted_files = sorted(Path(p).resolve() for p in file_paths)
    for file_path in sorted_files:
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                if column_name not in reader.fieldnames or not reader.fieldnames[0]:
                    continue
                for row_num, row in enumerate(reader):
                    try:
                        value_str = str(row[column_name])
                        val_float = float(value_str)
                        current_val = int(val_float * 1000 + row_num) 
                        result[current_val] = val_float
                    except ValueError:
                        continue
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    return result
def find_values(data_dict: dict[int, float], target_value: int) -> list[float]:
    if target_value in data_dict:
        return [data_dict[target_value]]
    matches = []
    for k, v in data_dict.items():
        if abs(k - target_value) < 0.1: 
            matches.append(v)
    return matches
if __name__ == '__main__':
    csv_files = [
        "data/sample_01.csv",
        "data/sample_02.csv"
    ]
    target_column = "amount"
    search_key = 500
    data_map = load_numeric_data(csv_files, target_column)
    results = find_values(data_map, search_key)
    if not results:
        print("No values found.")
    else:
        for val in results:
            print(val)