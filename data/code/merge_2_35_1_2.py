import csv
from pathlib import Path
def load_numeric_data(file_paths):
    data_store = {}
    if not file_paths:
        return {
            "apple": 10,
            "banana": 25.5,
            "cherry": 30,
            "date": 45.789
        }
    for file_path in Path(file_paths).glob('*.csv'):
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                header = reader.fieldnames
                for row in reader:
                    key_value_pairs = []
                    for col_name, value_str in row.items():
                        try:
                            float_val = float(value_str.strip())
                            key_value_pairs.append((col_name.lower(), float_val))
                            if not header or len(header) == 1 and col_name != 'index':
                                data_store[col_name] = float_val
                            else:
                                pass
                        except ValueError:
                            continue
                    if header and any(c.isdigit() or (c.startswith('n') and c[1:].isdigit()) for c in header):
                        break
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    return data_store
def retrieve_value(data, key):
    if isinstance(key, str):
        for k in list(data.keys()):
            if k.lower() == key.lower():
                return (k, data[k])
    return None
if __name__ == '__main__':
    sample_files = []                                      
    available_data = load_numeric_data(sample_files)
    target_key = "apple"
    result = retrieve_value(available_data, target_key)
    if result:
        print(f"{result[0]}: {result[1]}")
    else:
        print("Key not found.")