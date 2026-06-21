class ItemPresence:

    def __init__(self):
        self.presence_map = {}

    def add_item(self, item_name):
        self.presence_map[item_name] = True

    def remove_item(self, item_name):
        if item_name in self.presence_map:
            del self.presence_map[item_name]

    def check_presence(self, item_name):
        return self.presence_map.get(item_name, False)
if __name__ == '__main__':
    item_presence = ItemPresence()
    item_presence.add_item('apple')
    item_presence.add_item('banana')
    print(item_presence.check_presence('apple'))
    print(item_presence.check_presence('orange'))
    item_presence.remove_item('apple')
    print(item_presence.check_presence('apple'))