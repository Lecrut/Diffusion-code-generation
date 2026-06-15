class MembershipChecker:
    def __init__(self, member_list):
        self._members = set(member_list)
    def is_member(self, item):
        return item in self._members
if __name__ == '__main__':
    sample_members = ["Alice", "Bob", "Charlie", "David"]
    checker = MembershipChecker(sample_members)
    item1 = "Bob"
    item2 = "Eve"
    print(f"Is {item1} a member? {checker.is_member(item1)}")
    print(f"Is {item2} a member? {checker.is_member(item2)}")