import sys
def verify_key_existence(data_dict: dict, target_keys: list) -> bool:
    for key in target_keys:
        if not isinstance(key, str):
            raise TypeError("Keys must be strings.")
        if data_dict.get(key) is None and key not in data_dict:
            return False
    return True
def process_large_dataset(file_path: str = "data.json") -> dict:
    import json
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
if __name__ == '__main__':
    sample_data = {
        "user_id": 101,
        "username": "alice",
        "email": "alice@example.com",
        "role": "admin"
    }
    target_keys_to_check = ["user_id", "nonexistent_key"]
    if verify_key_existence(sample_data, target_keys_to_check):
        print("All keys exist.")
    else:
        missing_count = sum(1 for k in target_keys_to_check if k not in sample_data)
        print(f"Missing {missing_count} key(s).")