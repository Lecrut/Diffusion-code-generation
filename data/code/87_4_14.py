class Item:
    REQUIRED_PERMISSION = 'required_permission'

    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions

    @classmethod
    def is_eligible(cls, item):
        return item.active and cls.REQUIRED_PERMISSION in item.permissions
if __name__ == '__main__':
    sample_item1 = Item(active=True, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item1))
    sample_item2 = Item(active=False, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item2))
    sample_item3 = Item(active=True, permissions=[])
    print(Item.is_eligible(sample_item3))