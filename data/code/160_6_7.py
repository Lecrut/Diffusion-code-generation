class ItemPresenceMap:
    def __init__(self):
        self.presence_map = {}
    
    def add_item(self, item_name):
        if item_name not in self.presence_map:
            self.presence_map[item_name] = True
    
    def remove_item(self, item_name):
        if item_name in self.presence_map:
            del self.presence_map[item_name]
    
    def check_presence(self, item_name):
        return self.presence_map.get(item_name, False)

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    item_map = ItemPresenceMap()
    for item in sample_items:
        item_map.add_item(item)
    
    print(item_map.check_presence("banana"))
    print(item_map.check_presence("grape"))