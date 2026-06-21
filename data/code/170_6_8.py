import json

class InventoryItem:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class CustomEncoder(json.JSONEncoder):
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
        item = InventoryItem(item_data['id'], item_data['name'], item_data['quantity'])
        self.items.append(item)
    
    def get_all_items(self):
        return self.items

def serialize(data):
    return json.dumps(data, cls=CustomEncoder)

def deserialize(s):
    def object_hook(d):
        if '$ref' in d:
            return ref_dict[d['$ref']]
        return d
    ref_dict = {}
    objects = json.loads(s, object_hook=object_hook)
    for key, value in objects.items():
        if isinstance(value, dict) and '$ref' in value:
            ref_dict[value['$ref']] = objects[key]
    return objects

if __name__ == '__main__':
    manager = InventoryManager()
    item1 = {"id": 1, "name": "Apple", "quantity": 10}
    item2 = {"id": 2, "name": "Banana", "quantity": 5}
    item3 = {"id": 3, "name": "Orange", "quantity": 12}
    
    manager.add_item(item1)
    manager.add_item(item2)
    manager.add_item(item3)
    
    all_items_serialized = serialize(manager.get_all_items())
    print(all_items_serialized)
    
    deserialized_items = deserialize(all_items_serialized)
    for item in deserialized_items:
        print(f"ID: {item.id}, Name: {item.name}, Quantity: {item.quantity}")