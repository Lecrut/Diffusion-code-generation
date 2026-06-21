import json

def resolve_nested_path(data, path_str):
    keys = path_str.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list):
            try:
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    raise KeyError(key)
            except ValueError:
                raise KeyError(key)
        else:
            raise KeyError(key)
    return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "address": {
                    "city": "Metropolis"
                }
            }
        },
        "items": [
            {"id": 1, "name": "Alpha"},
            {"id": 2, "name": "Beta"}
        ]
    }
    
    result1 = resolve_nested_path(sample_data, "user.profile.address.city")
    print(result1)
    
    result2 = resolve_nested_path(sample_data, "items.1.name")
    print(result2)