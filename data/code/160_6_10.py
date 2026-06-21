class ItemPresenceMap:

    def __init__(self):
        self.map = {}

    def add_item(self, item_name):
        self.map[item_name] = True

    def remove_item(self, item_name):
        if item_name in self.map:
            del self.map[item_name]

    def check_presence(self, item_name):
        return self.map.get(item_name, False)
if __name__ == '__main__':
    ipm = ItemPresenceMap()
    ipm.add_item('apple')
    ipm.add_item('banana')
    print(ipm.check_presence('apple'))
    print(ipm.check_presence('orange'))
    ipm.remove_item('apple')
    print(ipm.check_presence('apple'))