import json
def update_json_file(file_path: str, new_entry: dict) -> None:
    try:
        if not isinstance(new_entry, dict):
            raise ValueError("New entry must be a dictionary.")
        existing_data = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
                if not isinstance(content, list):
                    raise ValueError("JSON root must be a list.")
                for item in content:
                    if not isinstance(item, dict):
                        raise ValueError("All items in the JSON array must be dictionaries.")
        except FileNotFoundError:
            existing_data = []
        except json.JSONDecodeError as e:
            print(f"Failed to parse {file_path}: {e}")
            return
        content.append(new_entry)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=4)
    except PermissionError:
        print(f"Permission denied accessing {file_path}")
if __name__ == '__main__':
    file_name = "data.json"
    new_item = {"id": 101, "name": "Alice", "status": "active"}
    update_json_file(file_name, new_item)