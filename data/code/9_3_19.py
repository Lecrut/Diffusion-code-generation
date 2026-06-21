import os
import json

def convert_volumes(volumes_liters: list) -> dict:
    cubic_meters = [vol / 1000.0 for vol in volumes_liters]
    return {'liters': volumes_liters, 'cubic_meters': cubic_meters}

def read_volumes_from_file(filepath: str) -> list:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'The file {filepath} does not exist.')
    with open(filepath, 'r') as file:
        content = file.read()
    if not content.strip():
        raise ValueError('The file is empty.')
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f'Invalid JSON in file: {e}', content, 0)
    if not isinstance(data, list):
        raise ValueError('JSON content must be a list of numbers.')
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError('All items in the list must be numbers.')
    return data

def process_volumes(volumes: list) -> dict:
    return convert_volumes(volumes)
if __name__ == '__main__':
    sample_data = [500, 1000, 2500.5, 0, -10]
    temp_filepath = 'sample_volumes.json'
    try:
        with open(temp_filepath, 'w') as f:
            json.dump(sample_data, f)
        volumes_liters = read_volumes_from_file(temp_filepath)
        result = process_volumes(volumes_liters)
        print('Volumes in Liters:', result['liters'])
        print('Volumes in Cubic Meters:', result['cubic_meters'])
        os.remove(temp_filepath)
    except FileNotFoundError as e:
        print(f'File error: {e}')
    except json.JSONDecodeError as e:
        print(f'JSON error: {e}')
    except ValueError as e:
        print(f'Value error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')