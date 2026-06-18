import json
def update_json_file(file_path: str, new_entry: dict) -> None:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file.")
        return
    if isinstance(data, dict):
        data[new_entry['key']] = new_entry['value']
    elif isinstance(data, list):
        data.append(new_entry)
    else:
        print("Error: Root element must be a dictionary or a list.")
        return
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
if __name__ == '__main__':
    file_name = "data.json"
    new_data = {
        "key": "new_entry",
        "value": 12345
    }
    update_json_file(file_name, new_data)