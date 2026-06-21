import json

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.objects = {}

    def default(self, obj):
        if id(obj) in self.objects:
            return {'$ref': str(id(obj))}
        self.objects[id(obj)] = obj
        return super().default(obj)

def serialize(data):
    return json.dumps(data, cls=CustomEncoder)

def deserialize(s):
    return json.loads(s, object_hook=lambda d: d if '$ref' not in d else data[d['$ref']])

if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': [2, 3],
        'c': {'d': 4}
    }
    serialized = serialize(sample_data)
    print(serialized)
    deserialized = deserialize(serialized)
    print(deserialized)