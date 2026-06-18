import json
def load_dataset(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return {item.get('name'): item for item in data} if isinstance(data, list) else {}
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        raise SystemExit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        raise SystemExit(2)
def check_name_exists(dataset, target_name):
    if isinstance(target_name, str):
        return target_name in dataset
    else:
        print("Error: Target name must be a string.")
        return False
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "name": "Alice", "age": 30},
        {"id": 102, "name": "Bob", "age": 25},
        {"id": 103, "name": "Charlie", "age": 35}
    ]
    dataset = load_dataset.__globals__['sample_data'] if 'load_dataset' in globals() else {}
    target_name = "Alice"
    exists = check_name_exists(dataset, target_name)
    print(f"Name '{target_name}' found: {exists}")