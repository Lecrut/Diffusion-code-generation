class Item:

    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions

    @classmethod
    def is_eligible(cls, item):
        return item.active and 'read' in item.permissions
if __name__ == '__main__':
    sample_item = Item(active=True, permissions=['read', 'write'])
    print(Item.is_eligible(sample_item))