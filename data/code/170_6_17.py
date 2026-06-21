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
    decoded_data = json.loads(s, object_hook=object_hook)
    for key, value in ref_dict.items():
        obj_id, attr = key.split('.')
        obj = eval(obj_id)
        setattr(obj, attr, value)
    return decoded_data
if __name__ == '__main__':
    item1 = {'id': 1, 'name': 'Apple', 'quantity': 10}
    item2 = {'id': 2, 'name': 'Banana', 'quantity': 5}
    item3 = {'id': 3, 'name': 'Orange', 'quantity': 12}
    data = {'items': [item1, item2, item3]}
    serialized_data = serialize(data)
    print('Serialized:', serialized_data)
    deserialized_data = deserialize(serialized_data)
    print('Deserialized:', deserialized_data)