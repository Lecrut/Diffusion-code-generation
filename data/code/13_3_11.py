import json

class NestedAccessor:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = json.loads(data)
        else:
            self.data = data

    def get(self, path, default=None):
        keys = path.split('.')
        current = self.data
        for key in keys:
            if isinstance(current, dict):
                if key in current:
                    current = current[key]
                else:
                    return default
            elif isinstance(current, list):
                try:
                    index = int(key)
                    if 0 <= index < len(current):
                        current = current[index]
                    else:
                        return default
                except ValueError:
                    return default
            else:
                return default
        return current

if __name__ == '__main__':
    sample_json = '{"user": {"profile": {"name": "Alice", "details": {"age": 30, "active": true}}, "roles": ["admin", "user"]}}'
    accessor = NestedAccessor(sample_json)
    print(accessor.get('user.profile.name'))
    print(accessor.get('user.profile.details.age'))
    print(accessor.get('user.roles.1'))
    print(accessor.get('user.profile.email', 'Not Found'))