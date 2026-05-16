class ItemChecker:
    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions
    def is_eligible(self):
        return self.active and self.permissions
if __name__ == '__main__':
    item1 = ItemChecker(active=True, permissions=True)
    item2 = ItemChecker(active=False, permissions=True)
    item3 = ItemChecker(active=True, permissions=False)
    item4 = ItemChecker(active=False, permissions=False)
    print(f"Item 1 eligible: {item1.is_eligible()}")
    print(f"Item 2 eligible: {item2.is_eligible()}")
    print(f"Item 3 eligible: {item3.is_eligible()}")
    print(f"Item 4 eligible: {item4.is_eligible()}")