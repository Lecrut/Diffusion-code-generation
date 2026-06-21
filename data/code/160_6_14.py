class ItemPresence:
    def __init__(self):
        self.presence = {}

    def add(self, item_name):
        self.presence[item_name] = True

    def remove(self, item_name):
        if item_name in self.presence:
            del self.presence[item_name]

    def check(self, item_name):
        return self.presence.get(item_name, False)

if __name__ == '__main__':
    item_presence = ItemPresence()
    item_presence.add('apple')
    item_presence.add('banana')
    print(item_presence.check('apple'))
    print(item_presence.check('grape'))
    item_presence.remove('apple')
    print(item_presence.check('apple'))