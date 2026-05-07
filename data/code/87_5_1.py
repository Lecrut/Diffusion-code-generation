class Item:
    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions
    @classmethod
    def is_eligible(cls, item):
        return item.active and item.permissions
if __name__ == '__main__':
    item1 = Item(True, True)
    item2 = Item(False, True)
    item3 = Item(True, False)
    item4 = Item(False, False)
    print(f"Item 1 eligible: {Item.is_eligible(item1)}")
    print(f"Item 2 eligible: {Item.is_eligible(item2)}")
    print(f"Item 3 eligible: {Item.is_eligible(item3)}")
    print(f"Item 4 eligible: {Item.is_eligible(item4)}")