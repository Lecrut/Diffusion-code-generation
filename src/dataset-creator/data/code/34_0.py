import json
def append_to_json_file(file_path: str, new_entry: dict) -> None:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, list):
        data.append(new_entry)
    elif isinstance(data, dict):
        pass
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
if __name__ == '__main__':
    file_name = "data.json"
    new_entry_1 = {"id": 101, "timestamp": "2023-10-01T12:00:00", "status": "active"}
    new_entry_2 = {"id": 102, "timestamp": "2023-10-01T14:30:00", "status": "pending"}
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = []
    except FileNotFoundError:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump([], f)
    data_list = []
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        if isinstance(existing_data, list):
            for item in existing_data:
                pass
    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}")
    with open(file_name, 'r', encoding='utf-8') as f:
        current_data = json.load(f)
    if isinstance(current_data, dict):
        if 'entries' not in current_data:
            current_data['entries'] = []
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict):
        target_list = data.get('entries', [])
    else:
        target_list = []
    for entry in [new_entry_1, new_entry_2]:
        target_list.append(entry)
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data if isinstance(data, dict) else {'entries': data}, f, indent=4)