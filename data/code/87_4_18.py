class Item:

    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions

    @classmethod
    def is_eligible(cls, item):
        if not item.active:
            return False
        if 'required_permission' not in item.permissions:
            return False
        return True
if __name__ == '__main__':
    sample_item1 = Item(active=True, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item1))
    sample_item2 = Item(active=False, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item2))
    sample_item3 = Item(active=True, permissions=['optional_permission'])
    print(Item.is_eligible(sample_item3))