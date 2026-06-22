import json
import copy

def get_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key not in current:
                raise KeyError(f"Key '{key}' not found in dictionary")
            current = current[key]
        elif isinstance(current, list):
            if not key.isdigit():
                raise TypeError(f"List index must be an integer, got '{key}'")
            index = int(key)
            if index < 0 or index >= len(current):
                raise IndexError(f"Index {index} out of range for list of length {len(current)}")
            current = current[index]
        else:
            raise TypeError(f"Cannot traverse into {type(current).__name__} with key '{key}'")
    return copy.deepcopy(current)

if __name__ == '__main__':
    sample_data = {
        "level1": {
            "level2": {
                "level3": [
                    {"value": "deep"},
                    {"value": "target"}
                ]
            },
            "other": "shallow"
        },
        "simple": 42
    }

    result = get_nested_value(sample_data, "level1.level2.level3.1.value")
    print(result)