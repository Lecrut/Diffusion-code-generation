import json
def load_dataset(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return set(data['names']) if isinstance(data.get('names'), list) else set()
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in dataset.")
        exit(1)
def check_name_exists(name, names_set):
    return name.lower() in [n.lower() for n in names_set]
if __name__ == '__main__':
    sample_data = {
        "names": ["Alice", "Bob Smith", "Charlie O'Connor"]
    }
    dataset_file = 'dataset.json'
    with open(dataset_file, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f)
    target_name = "alice"
    names_set = load_dataset(dataset_file)
    if check_name_exists(target_name, names_set):
        print(f"The name '{target_name}' exists in the dataset.")
    else:
        print(f"The name '{target_name}' does not exist in the dataset.")