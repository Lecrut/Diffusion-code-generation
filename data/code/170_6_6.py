import json

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.objects = []

    def default(self, obj):
        if id(obj) in self.objects:
            return f"__CIRCULAR_REF_{id(obj)}__"
        self.objects.append(id(obj))
        try:
            return super().default(obj)
        finally:
            self.objects.remove(id(obj))

def serialize(data):
    return json.dumps(data, cls=CustomEncoder)

def deserialize(s):
    def decode_circular_ref(dct):
        for k, v in dct.items():
            if isinstance(v, str) and v.startswith("__CIRCULAR_REF_"):
                dct[k] = [x for x in data_list if id(x) == int(v[len("__CIRCULAR_REF_"):])][0]
        return dct

    data_list = []
    def decode(dct):
        obj_id = dct.pop('__id__', None)
        if obj_id is not None:
            data_list[obj_id] = dct
        else:
            obj_id = len(data_list)
            data_list.append(dct)
        for k, v in dct.items():
            if isinstance(v, dict) and '__id__' in v:
                dct[k] = decode(v)
        return dct

    decoded_data = json.loads(s, object_hook=decode)
    decoded_data = decode_circular_ref(decoded_data)
    return data_list[0]

if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': [2, 3],
        'c': {'d': 4}
    }
    serialized_data = serialize(sample_data)
    print("Serialized:", serialized_data)
    deserialized_data = deserialize(serialized_data)
    print("Deserialized:", deserialized_data)