class Item:

    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions

    @classmethod
    def is_eligible(cls, item):
        return item.active and cls.has_sufficient_permissions(item)

    @staticmethod
    def has_sufficient_permissions(item):
        required_permissions = {'read', 'write'}
        return required_permissions.issubset(item.permissions)
if __name__ == '__main__':
    sample_item = Item(active=True, permissions={'read', 'write', 'execute'})
    print(Item.is_eligible(sample_item))