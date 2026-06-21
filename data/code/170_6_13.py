import json

class InventoryItem:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

class InventoryManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_all_items(self):
        return self.items

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        self.objects = {}
        super().__init__(*args, **kwargs)
    
    def default(self, obj):
        if isinstance(obj, InventoryItem):
            if id(obj) in self.objects:
                return {'$ref': f'#{self.objects[id(obj)]}'}
            self.objects[id(obj)] = len(self.objects)
            return {
                'item_id': obj.item_id,
                'name': obj.name,
                'quantity': obj.quantity
            }
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
    for obj in decoded_data.values():
        if isinstance(obj, dict):
            ref_dict[f"#{obj['item_id']}"] = InventoryItem(obj['item_id'], obj['name'], obj['quantity'])
    return decoded_data

if __name__ == '__main__':
    manager = InventoryManager()
    item1 = InventoryItem(1, "Apple", 10)
    item2 = InventoryItem(2, "Banana", 5)
    item3 = InventoryItem(3, "Orange", 12)
    
    manager.add_item(item1)
    manager.add_item(item2)
    manager.add_item(item3)
    
    serialized_data = serialize(manager.get_all_items())
    print(serialized_data)

    deserialized_data = deserialize(serialized_data)
    for item in deserialized_data.values():
        if isinstance(item, InventoryItem):
            print(f"Item ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}")