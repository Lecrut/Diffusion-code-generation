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
    decoded_data = json.loads(s, object_hook=lambda obj: {**obj, **object_hook(obj)})
    
    for key, value in decoded_data.items():
        if isinstance(value, dict) and '$ref' in value:
            ref_dict[value['$ref']] = decoded_data[key]
    
    return decoded_data

if __name__ == '__main__':
    data = {
        'id': 1,
        'name': "Apple",
        'quantity': 10,
        'self': None
    }
    data['self'] = data
    
    serialized = serialize(data)
    print("Serialized:", serialized)
    
    deserialized = deserialize(serialized)
    print("Deserialized:", deserialized)