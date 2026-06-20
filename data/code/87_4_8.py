class Item:

    def __init__(self, active: bool, permissions: int):
        self.active = active
        self.permissions = permissions

    @classmethod
    def is_eligible(cls, item: 'Item') -> bool:
        return item.active and item.permissions & 7 == 7
if __name__ == '__main__':
    sample_item = Item(active=True, permissions=7)
    print(Item.is_eligible(sample_item))