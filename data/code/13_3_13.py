import json
import sys

def get_nested_value(data, path):
    if not isinstance(data, (dict, list)):
        raise TypeError("Data must be a JSON-like object")
    
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    
    keys = path.split('.')
    current = data
    
    for key in keys:
        if isinstance(current, dict):
            if key in current:
                current = current[key]
            else:
                raise KeyError(f"Key '{key}' not found")
        elif isinstance(current, list):
            try:
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    raise IndexError(f"Index '{key}' out of range")
            except ValueError:
                raise TypeError(f"Index must be an integer, got '{key}'")
        else:
            raise TypeError(f"Cannot access key '{key}' on {type(current).__name__}")
            
    return current

def main():
    sample_data = {
        "user": {
            "profile": {
                "name": "Alice",
                "age": 30,
                "addresses": [
                    {"city": "New York", "zip": "10001"},
                    {"city": "London", "zip": "SW1A 1AA"}
                ]
            }
        },
        "config": {
            "debug": True,
            "settings": {
                "theme": "dark",
                "language": "en"
            }
        }
    }
    
    result1 = get_nested_value(sample_data, "user.profile.name")
    print(result1)
    
    result2 = get_nested_value(sample_data, "user.profile.addresses.0.city")
    print(result2)
    
    result3 = get_nested_value(sample_data, "config.settings.theme")
    print(result3)

if __name__ == '__main__':
    main()