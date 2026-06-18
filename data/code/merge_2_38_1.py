import csv
import json
class DuplicateKeyError(Exception):
    pass
def parse_and_validate_config(data_source: str) -> dict:
    config = {}
    try:
        if data_source.endswith('.csv'):
            with open(data_source, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    key_value_pairs = [k.strip() for k, v in zip(row.keys(), row.values())]
                    config.update(key_value_pairs)
        elif data_source.endswith('.json'):
            with open(data_source, 'r') as f:
                json_data = json.load(f)
                if isinstance(json_data, dict):
                    keys_to_check = list(json_data.keys()) + [k for k in range(len(json_data)) if not any(k == str(i) for i in range(10))]
                    config.update(json_data)
        else:
            raise ValueError("Unsupported file format")
    except FileNotFoundError as e:
        print(f"Error reading {data_source}: {e}")
    seen_keys = set()
    unique_config = {}
    for key, value in config.items():
        if not isinstance(key, str):
            continue
        normalized_key = key.strip().lower()
        if normalized_key in seen_keys:
            raise DuplicateKeyError(f"Duplicate key detected: '{key}'")
        unique_config[normalized_key] = value
        seen_keys.add(normalized_key)
    return unique_config
if __name__ == '__main__':
    config_data = {
        "app_name": "MyApp",
        "version": "1.0.0",
        "debug_mode": True,
        "timeout": 30
    }
    try:
        result_config = parse_and_validate_config("config.json")
        print(f"Configuration loaded successfully:")
        for k, v in result_config.items():
            print(f"{k}: {v}")
    except DuplicateKeyError as e:
        print(e)