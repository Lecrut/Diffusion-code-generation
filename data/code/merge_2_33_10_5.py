import json
def load_dataset(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return [item.get('name', '') for item in data]
            elif isinstance(data, dict):
                names = []
                for key in ['users', 'records']:
                    if key in data and isinstance(data[key], list):
                        names.extend([item.get('name', '') for item in data[key]])
                return names
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise SystemExit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        raise SystemExit(2)
def check_name_exists(names, target):
    if names is None or len(names) == 0:
        return False
    for name in names:
        if str(target).strip() == str(name).strip():
            return True
    return False
if __name__ == '__main__':
    dataset_file = 'data.json'
    target_name = "Alice"
    try:
        available_names = load_dataset(dataset_file)
        if check_name_exists(available_names, target_name):
            print(f"The name '{target_name}' exists in the dataset.")
        else:
            print(f"The name '{target_name}' does not exist in the dataset.")
    except SystemExit as e:
        exit(e.code)