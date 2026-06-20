class Item:
    def __init__(self, is_active, permissions):
        self.is_active = is_active
        self.permissions = permissions

    @classmethod
    def is_eligible(cls, item):
        return item.is_active and 'required_permission' in item.permissions

if __name__ == '__main__':
    sample_item = Item(is_active=True, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item))