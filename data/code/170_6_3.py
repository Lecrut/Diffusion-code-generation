import json

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        self.objects = {}
        super().__init__(*args, **kwargs)

    def default(self, obj):
        if id(obj) in self.objects:
            return {'$ref': f'#{self.objects[id(obj)]}'}
        self.objects[id(obj)] = len(self.objects)
        return super().default(obj)

def serialize(data):
    return json.dumps(data, cls=CustomEncoder)

def deserialize(s):
    def object_hook(d):
        if '$ref' in d:
            return ref_dict[d['$ref']]
        return d

    ref_dict = {}
    data = json.loads(s, object_hook=object_hook)
    for obj_id, index in CustomEncoder.objects.items():
        ref_dict[f'#{index}'] = data
    return data

if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': {'c': 2},
        'd': [3, 4]
    }
    serialized = serialize(sample_data)
    deserialized = deserialize(serialized)
    print(deserialized)