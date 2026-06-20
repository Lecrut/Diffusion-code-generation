class Item:

    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions

    def is_eligible(self):
        return self.active and 'read' in self.permissions
if __name__ == '__main__':
    item1 = Item(True, ['read', 'write'])
    print(item1.is_eligible())
    item2 = Item(False, ['read'])
    print(item2.is_eligible())
    item3 = Item(True, ['write'])
    print(item3.is_eligible())