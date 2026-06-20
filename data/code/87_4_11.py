class Item:

    def __init__(self, is_active, permissions):
        self.is_active = is_active
        self.permissions = permissions

    def is_eligible(self):
        return self.is_active and 'required_permission' in self.permissions
if __name__ == '__main__':
    item1 = Item(True, {'required_permission': True})
    print(item1.is_eligible())
    item2 = Item(False, {'required_permission': True})
    print(item2.is_eligible())
    item3 = Item(True, {'other_permission': True})
    print(item3.is_eligible())