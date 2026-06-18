import json
def append_to_json_file(file_path: str, new_entry: dict) -> None:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, list):
        data.append(new_entry)
    elif isinstance(data, dict):
        entries_key = 'entries'
        if entries_key not in data:
            data[entries_key] = []
        if new_entry is None and len(new_entry) == 0:
             return
        try:
            data[entries_key].append(new_entry)
        except TypeError:
             raise ValueError("The new entry must be a dictionary.")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    file_name = "data.json"
    new_data_1 = {"id": 101, "name": "Alice", "score": 95}
    new_data_2 = {"id": 102, "name": "Bob", "score": 87}
    try:
        if not __import__('os').path.exists(file_name):
            initial_structure = {
                "entries": []
            }
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(initial_structure, f)
        append_to_json_file(file_name, new_data_1)
        append_to_json_file(file_name, new_data_2)
    except FileNotFoundError as e:
        print(f"Error reading file {file_name}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")