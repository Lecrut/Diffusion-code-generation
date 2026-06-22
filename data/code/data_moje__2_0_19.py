import os
import json

def calculate_total_volume(file_path: str) -> float:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f'Invalid JSON in {file_path}: {e.msg}', e.doc, e.pos)
    if not isinstance(data, list):
        raise ValueError('JSON root must be a list')
    total = 0.0
    for i, item in enumerate(data):
        if isinstance(item, (int, float)) and (not isinstance(item, bool)):
            total += item
        elif isinstance(item, dict) and 'value' in item:
            val = item['value']
            if isinstance(val, (int, float)) and (not isinstance(val, bool)):
                total += val
            else:
                raise ValueError(f'Invalid value type at index {i}')
        else:
            raise ValueError(f'Invalid item type at index {i}: {type(item)}')
    return total

def create_sample_file():
    sample_data = [{'value': 10.5}, {'value': 20.3}, {'value': 15.7}, {'value': 30.0}, {'value': 25.1}]
    sample_file = 'sample_volumes.json'
    with open(sample_file, 'w') as f:
        json.dump(sample_data, f)
    return sample_file
if __name__ == '__main__':
    sample_file = create_sample_file()
    try:
        total_volume = calculate_total_volume(sample_file)
        print(f'Total volume: {total_volume}')
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        print(f'Error: {e}')
    finally:
        if os.path.exists(sample_file):
            os.remove(sample_file)