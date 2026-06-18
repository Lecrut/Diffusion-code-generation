import json
def load_dataset(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data.get('names', []))
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        raise SystemExit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in dataset.")
        raise SystemExit(2)
def check_name_exists(name, name_set):
    if not isinstance(name, str):
        return False
    return name.lower() in [n.lower() for n in name_set]
if __name__ == '__main__':
    sample_data = {
        "names": ["Alice", "Bob", "Charlie"]
    }
    dataset_file = 'sample_dataset.json'
    try:
        if check_name_exists("alice", sample_data["names"]):
            print("Name exists in the dataset.")
        else:
            print("Name does not exist in the dataset.")
    except SystemExit as e:
        exit(e.code)