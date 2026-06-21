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
    try:
        return json.dumps(data, cls=CustomEncoder)
    except TypeError as e:
        print(f"Serialization error: {e}")
        return None

def deserialize(s):
    def object_hook(d):
        if '$ref' in d:
            return ref_dict[d['$ref']]
        return d
    
    try:
        ref_dict = {}
        data = json.loads(s, object_hook=object_hook)
        for key, value in ref_dict.items():
            ref_dict[key] = data[value]
        return data
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Deserialization error: {e}")
        return None

if __name__ == '__main__':
    item1 = {"id": 1, "name": "Apple", "quantity": 10}
    item2 = {"id": 2, "name": "Banana", "quantity": 5}
    item3 = {"id": 3, "name": "Orange", "quantity": 12}
    
    serialized_data = serialize([item1, item2, item3])
    print("Serialized:", serialized_data)
    
    deserialized_data = deserialize(serialized_data)
    print("Deserialized:", deserialized_data)