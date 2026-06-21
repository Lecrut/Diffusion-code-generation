class MembershipChecker:
    def __init__(self, items):
        self.items = set(items)

    def is_member(self, item):
        return item in self.items

if __name__ == '__main__':
    checklist = MembershipChecker(["Alice", "Bob", "Charlie"])
    print(f"Is Alice a member? {checklist.is_member('Alice')}")
    print(f"Is Eve a member? {checklist.is_member('Eve')}")