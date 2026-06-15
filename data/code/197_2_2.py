class MembershipChecker:
    def __init__(self, members):
        self._members = set(members)
    def is_member(self, item):
        return item in self._members
if __name__ == '__main__':
    sample_members = ["Alice", "Bob", "Charlie", "David"]
    checker = MembershipChecker(sample_members)
    print(f"Is Alice a member? {checker.is_member('Alice')}")
    print(f"Is Eve a member? {checker.is_member('Eve')}")
    print(f"Is Charlie a member? {checker.is_member('Charlie')}")
    print(f"Is Frank a member? {checker.is_member('Frank')}")