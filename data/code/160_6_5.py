class ItemPresenceMap:
    def __init__(self):
        self.presence_map = {}
    
    @staticmethod
    def _is_valid_item(item_name):
        return isinstance(item_name, str) and item_name

    def add_item(self, item_name):
        if self._is_valid_item(item_name):
            self.presence_map[item_name] = True
    
    def remove_item(self, item_name):
        if item_name in self.presence_map:
            del self.presence_map[item_name]
    
    def check_presence(self, item_name):
        return self.presence_map.get(item_name, False)

if __name__ == '__main__':
    item_map = ItemPresenceMap()
    item_map.add_item('apple')
    item_map.add_item('banana')
    print(item_map.check_presence('apple'))
    print(item_map.check_presence('grape'))
    item_map.remove_item('apple')
    print(item_map.check_presence('apple'))