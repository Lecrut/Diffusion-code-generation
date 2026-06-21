import json
ITEM_REF_KEY = '$ref'
REF_PREFIX = '#'

class CustomEncoder(json.JSONEncoder):

    def __init__(self, *args, **kwargs):
        self.objects = {}
        super().__init__(*args, **kwargs)

    def default(self, obj):
        if id(obj) in self.objects:
            return {ITEM_REF_KEY: f'{REF_PREFIX}{self.objects[id(obj)]}'}
        self.objects[id(obj)] = len(self.objects)
        return super().default(obj)

def serialize(data):
    return json.dumps(data, cls=CustomEncoder)

def deserialize(s):

    def object_hook(d):
        if ITEM_REF_KEY in d:
            ref_index = int(d[ITEM_REF_KEY].strip(REF_PREFIX))
            ref_obj = ref_dict[ref_index]
            ref_dict[id(ref_obj)] = ref_obj
            return ref_obj
        return d
    ref_dict = {}
    decoded_data = json.loads(s, object_hook=object_hook)
    for ref_index in sorted(ref_dict.keys(), reverse=True):
        obj_id = id(ref_dict[ref_index])
        while ref_dict[obj_id][ITEM_REF_KEY]:
            ref_id = int(ref_dict[obj_id][ITEM_REF_KEY].strip(REF_PREFIX))
            ref_obj = ref_dict[ref_id]
            ref_dict[obj_id] = ref_obj
    return decoded_data
if __name__ == '__main__':
    item1 = {'id': 1, 'name': 'Apple', 'quantity': 10}
    item2 = {'id': 2, 'name': 'Banana', 'quantity': 5}
    item3 = {'id': 3, 'name': 'Orange', 'quantity': 12}
    item1['item'] = item2
    item2['item'] = item3
    serialized_data = serialize(item1)
    print(serialized_data)
    deserialized_data = deserialize(serialized_data)
    print(deserialized_data)