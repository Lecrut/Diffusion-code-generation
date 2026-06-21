class ChecklistMembershipChecker:
    def __init__(self, items):
        self.items_set = set(items)

    def is_member(self, item):
        return item in self.items_set

if __name__ == '__main__':
    checker = ChecklistMembershipChecker(["Alice", "Bob", "Charlie"])
    print(f"Is Alice a member? {checker.is_member('Alice')}")
    print(f"Is Bob a member? {checker.is_member('Bob')}")
    print(f"Is Eve a member? {checker.is_member('Eve')}")