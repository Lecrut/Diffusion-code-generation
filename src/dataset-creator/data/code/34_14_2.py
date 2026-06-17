import json
def update_json_file(file_path: str) -> None:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file.")
        return
    new_entry = {
        "id": 101,
        "name": "New Item",
        "status": "active"
    }
    if isinstance(data, list):
        data.append(new_entry)
    elif isinstance(data, dict):
        existing_keys = set(data.keys())
        new_key_set = {new_entry["id"]} & existing_keys
        for key in new_key_set:
            data[key].update(new_entry)
        if not new_key_set and "entries" not in data:
            data.setdefault("entries", []).append(new_entry)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
if __name__ == '__main__':
    update_json_file('data.json')