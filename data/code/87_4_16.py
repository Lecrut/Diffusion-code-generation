class Item:

    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions

    def is_eligible(self):
        return self.active and 'required_permission' in self.permissions
if __name__ == '__main__':
    item1 = Item(active=True, permissions=['required_permission', 'optional_permission'])
    print(item1.is_eligible())
    item2 = Item(active=False, permissions=['optional_permission'])
    print(item2.is_eligible())