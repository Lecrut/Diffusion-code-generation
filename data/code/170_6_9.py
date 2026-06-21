import json

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.objects = {}

    def default(self, obj):
        if id(obj) in self.objects:
            return {"$ref": f"#{self.objects[id(obj)]}"}
        self.objects[id(obj)] = len(self.objects)
        return super().default(obj)

def deserialize(data):
    objects = {}
    for key, value in data.items():
        if isinstance(value, dict) and "$ref" in value:
            objects[key] = objects[value["$ref"][1:]]
        else:
            objects[key] = value
    return objects

if __name__ == '__main__':
    sample_data = {
        "a": {"b": 2},
        "c": {"d": 4}
    }
    serialized_data = json.dumps(sample_data, cls=CustomEncoder)
    print(serialized_data)
    deserialized_data = deserialize(json.loads(serialized_data))
    print(deserialized_data)