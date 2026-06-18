import json
def load_dataset(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data['names']) if isinstance(data.get('names'), list) else set()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise SystemExit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{file_path}'. {e}")
        raise SystemExit(2)
def check_name_exists(name, name_set):
    if isinstance(name, str):
        return name.lower() in [n.lower() for n in name_set]
    else:
        print("Warning: Name must be a string.")
        return False
if __name__ == '__main__':
    dataset_file = 'dataset.json'
    target_name = "john doe"
    try:
        available_names = load_dataset(dataset_file)
        if check_name_exists(target_name, available_names):
            print(f"The name '{target_name}' exists in the dataset.")
        else:
            print(f"The name '{target_name}' does not exist in the dataset.")
    except SystemExit as e:
        exit(e.code)