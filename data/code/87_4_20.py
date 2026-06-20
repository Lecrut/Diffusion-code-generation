class Item:

    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions

    def is_eligible(self):
        return self.active and 'required_permission' in self.permissions
if __name__ == '__main__':
    item1 = Item(True, {'required_permission', 'other_permission'})
    print(item1.is_eligible())
    item2 = Item(False, {'required_permission', 'other_permission'})
    print(item2.is_eligible())
    item3 = Item(True, {'other_permission'})
    print(item3.is_eligible())