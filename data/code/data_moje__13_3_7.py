import json

def get_nested_value(data, path):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list):
            try:
                index = int(key)
                current = current[index]
            except (ValueError, IndexError):
                raise KeyError(f"Index '{key}' out of range or invalid")
        else:
            raise KeyError(f"Key or index '{key}' not found")
    return current

if __name__ == '__main__':
    sample_data = {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "address": {
                    "city": "Wonderland",
                    "zip": "12345"
                }
            },
            {
                "id": 2,
                "name": "Bob",
                "address": {
                    "city": "Nowhere",
                    "zip": "67890"
                }
            }
        ]
    }
    
    path1 = "users.0.name"
    path2 = "users.1.address.city"
    path3 = "users.0.address.zip"
    
    print(get_nested_value(sample_data, path1))
    print(get_nested_value(sample_data, path2))
    print(get_nested_value(sample_data, path3))