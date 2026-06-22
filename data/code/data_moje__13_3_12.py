import json
from functools import reduce

def get_nested_value(data, path):
    if not path:
        return data
    keys = path.split('.')
    try:
        return reduce(lambda acc, key: acc[key], keys, data)
    except (KeyError, IndexError, TypeError):
        return None

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "name": "Alice",
                "contact": {
                    "email": "alice@example.com",
                    "phones": ["555-0100", "555-0101"]
                }
            },
            "settings": {
                "theme": "dark",
                "notifications": True
            }
        },
        "status": "active"
    }

    path1 = "user.profile.contact.email"
    path2 = "user.profile.contact.phones.1"
    path3 = "user.profile.age"
    path4 = "status"

    result1 = get_nested_value(sample_data, path1)
    result2 = get_nested_value(sample_data, path2)
    result3 = get_nested_value(sample_data, path3)
    result4 = get_nested_value(sample_data, path4)

    print(result1)
    print(result2)
    print(result3)
    print(result4)