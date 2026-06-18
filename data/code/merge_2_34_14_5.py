import json
def update_json_file(file_path: str) -> None:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        new_entry = {
            "id": 1001,
            "name": "New Item",
            "status": "active"
        }
        if isinstance(data, list):
            data.append(new_entry)
        elif isinstance(data, dict):
            data["entries"] = [data.get("entries", [])] + [new_entry]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
    except IOError as e:
        print(f"I/O error occurred while processing file: {e}")
if __name__ == '__main__':
    update_json_file("data.json")