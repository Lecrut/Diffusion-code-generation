class Item:
    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions
    @classmethod
    def is_eligible(cls, item):
        return item.active and item.permissions
if __name__ == '__main__':
    item1 = Item(active=True, permissions=10)
    item2 = Item(active=False, permissions=10)
    item3 = Item(active=True, permissions=5)
    print(f"Item 1 eligible: {Item.is_eligible(item1)}")
    print(f"Item 2 eligible: {Item.is_eligible(item2)}")
    print(f"Item 3 eligible: {Item.is_eligible(item3)}")