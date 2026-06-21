class ItemPresenceMap:
    def __init__(self):
        self.presence_map = {}
    
    @staticmethod
    def create_from_items(items):
        instance = ItemPresenceMap()
        for item in items:
            if item:
                instance.presence_map[item] = True
        return instance
    
    def add_item(self, item_name):
        self.presence_map[item_name] = True
    
    def remove_item(self, item_name):
        if item_name in self.presence_map:
            del self.presence_map[item_name]
    
    def check_presence(self, item_name):
        return self.presence_map.get(item_name, False)

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    item_map = ItemPresenceMap.create_from_items(sample_items)
    print(item_map.check_presence('apple'))
    print(item_map.check_presence('grape'))
    item_map.add_item('grape')
    print(item_map.check_presence('grape'))
    item_map.remove_item('banana')
    print(item_map.check_presence('banana'))