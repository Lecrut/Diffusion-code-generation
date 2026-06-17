import json
def update_json_file(filepath: str, new_entry: dict) -> None:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, list):
            data.append(new_entry)
        elif isinstance(data, dict):
            for key in new_entry.keys():
                if key not in data:
                    data[key] = []
                data[key].append(new_entry.get(key))
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in file. {e}")
    except IOError as e:
        print(f"IO Error occurred while processing the file: {e}")
if __name__ == '__main__':
    sample_entry = {"id": 101, "name": "New Item", "status": "active"}
    try:
        update_json_file("data.json", sample_entry)
        print("JSON file updated successfully.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")