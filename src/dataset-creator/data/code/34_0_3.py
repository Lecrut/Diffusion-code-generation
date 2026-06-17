import json
def append_to_json_file(file_path: str, new_entry) -> None:
    with open(file_path, 'r') as f:
        data = json.load(f)
    if isinstance(data, list):
        data.append(new_entry)
    elif isinstance(data, dict):
        for key in data.keys():
            if isinstance(data[key], list):
                data[key].append(new_entry)
                break
            else:
                data[key] = [data[key]]
                data[key].append(new_entry)
    else:
        raise ValueError(f"Unsupported JSON structure type: {type(data)}")
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
if __name__ == '__main__':
    sample_data = {"timestamp": "2023-10-27T10:00:00", "event_id": 98765}
    file_path = 'data.json'
    append_to_json_file(file_path, sample_data)