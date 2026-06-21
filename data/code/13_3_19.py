import json

class NestedAccessor:
    def __init__(self, data):
        self.data = data

    def get(self, path):
        keys = path.split('.')
        current = self.data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            elif isinstance(current, list) and key.isdigit():
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    raise KeyError(f"Index {index} out of range for list")
            else:
                raise KeyError(f"Key '{key}' not found in path: {'.'.join(keys)}")
        return current

if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "contact": {
                    "email": "alice@example.com"
                },
                "address": {
                    "city": "New York",
                    "zip": "10001"
                }
            },
            "orders": [
                {"id": 101, "item": "Book"},
                {"id": 102, "item": "Pen"}
            ]
        },
        "status": "active"
    }

    accessor = NestedAccessor(sample_data)
    
    print(accessor.get("user.profile.contact.email"))
    print(accessor.get("user.orders.1.item"))
    print(accessor.get("status"))