import json
def append_to_json_file(file_path: str, new_entry: dict) -> None:
    with open(file_path, 'r') as f:
        data = json.load(f)
    if isinstance(data, list):
        data.append(new_entry)
    elif isinstance(data, dict):
        for key in ['entries', 'data']:
            if key in data and not isinstance(data[key], list):
                new_list = []
                existing_entries = data.get(key, [])
                if isinstance(existing_entries, list):
                    new_list.extend(existing_entries)
                else:
                    new_list.append(existing_entries)
                data[key] = new_list + [new_entry]
                break
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
if __name__ == '__main__':
    sample_data = {
        "id": 1001,
        "timestamp": "2023-10-05T14:30:00",
        "status": "active"
    }
    append_to_json_file("data.json", sample_data)