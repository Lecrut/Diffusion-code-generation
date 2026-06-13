class MembershipChecker:
    def __init__(self):
        self.memberships = set()
    def add_member(self, member_id):
        self.memberships.add(member_id)
    def has_member(self, member_id):
        return member_id in self.memberships
if __name__ == '__main__':
    checker = MembershipChecker()
    group_a_members = {101, 102, 103, 104, 105}
    group_b_members = {104, 105, 106, 107, 108}
    checker.memberships.update(group_a_members)
    checker.memberships.update(group_b_members)
    print(f"Checking if member 103 is a member: {checker.has_member(103)}")
    print(f"Checking if member 106 is a member: {checker.has_member(106)}")
    print(f"Checking if member 999 is a member: {checker.has_member(999)}")