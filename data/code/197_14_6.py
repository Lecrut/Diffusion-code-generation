class MembershipChecker:
    def __init__(self):
        self.memberships = set()
    def add_member(self, member_id):
        self.memberships.add(member_id)
    def check_membership(self, member_id):
        return member_id in self.memberships
if __name__ == '__main__':
    checker = MembershipChecker()
    group_a_members = {101, 102, 103, 104, 105}
    group_b_members = {103, 104, 105, 106, 107}
    checker.memberships.update(group_a_members)
    checker.memberships.update(group_b_members)
    print(f"Checking membership for member 103: {checker.check_membership(103)}")
    print(f"Checking membership for member 101: {checker.check_membership(101)}")
    print(f"Checking membership for member 999: {checker.check_membership(999)}")