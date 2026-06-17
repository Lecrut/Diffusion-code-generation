import json
def validate_and_append(data: dict) -> bool:
    if not isinstance(data, dict):
        return False
    required_keys = ['id', 'name']
    for key in required_keys:
        if key not in data or not isinstance(data[key], str):
            return False
    try:
        int(id_val)
    except ValueError:
        return False
    global storage
    storage.append({'id': id_val, 'name': name})
    return True
storage = []
if __name__ == '__main__':
    sample_data_1 = {'id': 101, 'name': 'Alice'}
    sample_data_2 = {'id': 102, 'name': 'Bob', 'extra': 'field'}
    validate_and_append(sample_data_1)
    if not validate_and_append(sample_data_2):
        print("Validation failed for second entry")