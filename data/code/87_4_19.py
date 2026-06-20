class Item:
    REQUIRED_PERMISSION = 'required_permission'

    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions

    @staticmethod
    def has_required_permission(permissions):
        return Item.REQUIRED_PERMISSION in permissions

    @classmethod
    def is_eligible(cls, item):
        return item.active and cls.has_required_permission(item.permissions)
if __name__ == '__main__':
    sample_item1 = Item(active=True, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item1))
    sample_item2 = Item(active=False, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item2))
    sample_item3 = Item(active=True, permissions=['other_permission'])
    print(Item.is_eligible(sample_item3))