import json

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.objects = {}

    def default(self, obj):
        if id(obj) in self.objects:
            return {'$ref': self.objects[id(obj)]}
        self.objects[id(obj)] = len(self.objects)
        return super().default(obj)

def serialize(data):
    encoder = CustomEncoder()
    return json.dumps(data, cls=encoder)

def deserialize(json_str):
    def object_hook(dct):
        if '$ref' in dct:
            return objects[dct['$ref']]
        return dct

    objects = {}
    data = json.loads(json_str, object_hook=object_hook)
    for i, obj in enumerate(objects.values()):
        setattr(obj, '__id__', i)
    return data

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