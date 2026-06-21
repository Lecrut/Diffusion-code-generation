import json

class CircularEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        self.objects = {}
        super().__init__(*args, **kwargs)
    
    def default(self, obj):
        if id(obj) in self.objects:
            return {'$ref': f'#{self.objects[id(obj)]}'}
        self.objects[id(obj)] = len(self.objects)
        return super().default(obj)

class InventoryManager:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_data):
        self.items.append(item_data)
    
    def get_all_items(self):
        return self.items

def serialize(data):
    return json.dumps(data, cls=CircularEncoder)

def deserialize(s):
    def object_hook(d):
        if '$ref' in d:
            return ref_dict[d['$ref']]
        return d
    ref_dict = {}
    for idx, obj in enumerate(json.loads(s, object_hook=object_hook)):
        ref_dict[f'#{idx}'] = obj
    return obj

if __name__ == '__main__':
    manager = InventoryManager()
    item1 = {"id": 1, "name": "Apple", "quantity": 10}
    item2 = {"id": 2, "name": "Banana", "quantity": 5}
    item3 = {"id": 3, "name": "Orange", "quantity": 12}
    manager.add_item(item1)
    manager.add_item(item2)
    manager.add_item(item3)
    all_items = manager.get_all_items()
    
    serialized = serialize(all_items)
    print(serialized)
    
    deserialized = deserialize(serialized)
    print(deserialized)