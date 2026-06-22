import json
import os

def process_volume_data(filename):
    results = []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    if not isinstance(data, list):
        return []
    for item in data:
        if not isinstance(item, (int, float)):
            continue
        liters = item * 0.001
        cubic_meters = item * 1e-06
        results.append((item, liters, cubic_meters))
    return results
if __name__ == '__main__':
    sample_filename = 'volumes.json'
    sample_data = [1000, 5000, 25000, 100000]
    with open(sample_filename, 'w') as f:
        json.dump(sample_data, f)
    converted_values = process_volume_data(sample_filename)
    for original, liters, cubic_meters in converted_values:
        print(f'{original} ml -> {liters} liters -> {cubic_meters} m³')
    os.remove(sample_filename)