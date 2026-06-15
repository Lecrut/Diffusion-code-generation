class MembershipChecker:
    def __init__(self):
        self.memberships = set()
    def add_member(self, member_id):
        self.memberships.add(member_id)
    def check_membership(self, member_id):
        return member_id in self.memberships
if __name__ == '__main__':
    checker = MembershipChecker()
    initial_members = [101, 102, 103, 104, 105, 106, 107]
    for member in initial_members:
        checker.add_member(member)
    print(f"Checking membership for 103: {checker.check_membership(103)}")
    print(f"Checking membership for 999: {checker.check_membership(999)}")
    print(f"Checking membership for 101: {checker.check_membership(101)}")