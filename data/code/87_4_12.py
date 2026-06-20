class Item:
    def __init__(self, active, permissions):
        if not isinstance(active, bool) or not isinstance(permissions, list):
            raise ValueError("Invalid input types")
        self.active = active
        self.permissions = permissions

    @classmethod
    def is_eligible(cls, item):
        return item.active and 'required_permission' in item.permissions

if __name__ == '__main__':
    sample_item = Item(active=True, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item))