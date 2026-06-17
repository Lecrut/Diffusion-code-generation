import csv
from pathlib import Path
def load_numeric_data(file_paths: list[str]) -> dict[int, float]:
    data_map = {}
    for file_path in file_paths:
        with open(file_path, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or 'id' not in reader.fieldnames:
                continue
            for row in reader:
                try:
                    record_id = int(row['id'])
                    value = float(row['value'])
                    data_map[record_id] = value
                except (ValueError, KeyError):
                    pass
    return data_map
def find_values(data_map: dict[int, float], target_ids: list[int]) -> list[tuple[int, float]]:
    results = []
    for record_id in target_ids:
        if record_id in data_map:
            results.append((record_id, data_map[record_id]))
    return results
if __name__ == '__main__':
    file_paths = ['data/sample1.csv', 'data/sample2.csv']
    sample_data = [
        {'id': 101, 'value': 3.14},
        {'id': 102, 'value': 2.71}
    ]
    for file_path in file_paths:
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'value'])
                writer.writeheader()
                writer.writerows(sample_data)
        except FileNotFoundError:
            pass
    data_map = load_numeric_data(file_paths)
    target_ids = [101]
    results = find_values(data_map, target_ids)
    print(results)