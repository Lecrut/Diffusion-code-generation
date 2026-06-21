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
        print(f"Error serializing data: {e}")
        return None

def deserialize(s):
    def object_hook(d):
        if '$ref' in d:
            return ref_dict[d['$ref']]
        return d
    
    try:
        ref_dict = {}
        obj = json.loads(s, object_hook=object_hook)
        return obj
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

if __name__ == '__main__':
    data = {
        "id": 1,
        "name": "Apple",
        "quantity": 10,
        "category": {
            "id": 2,
            "name": "Fruit"
        }
    }
    
    serialized_data = serialize(data)
    print("Serialized Data:", serialized_data)
    
    deserialized_data = deserialize(serialized_data)
    print("Deserialized Data:", deserialized_data)