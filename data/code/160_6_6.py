class ItemPresenceMap:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name):
        self.items[item_name] = True

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def check_presence(self, item_name):
        return item_name in self.items
if __name__ == '__main__':
    map = ItemPresenceMap()
    map.add_item('apple')
    map.add_item('banana')
    print(map.check_presence('apple'))
    print(map.check_presence('orange'))
    map.remove_item('apple')
    print(map.check_presence('apple'))