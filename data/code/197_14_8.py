import sys
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
    print("--- Initial Membership Check ---")
    test_members = [101, 103, 108, 999]
    for member in test_members:
        result = checker.check_membership(member)
        print(f"Is {member} a member? {result}")
    print("\n--- Adding More Members ---")
    new_members = [108, 109, 110]
    for member in new_members:
        checker.add_member(member)
    print("\n--- Updated Membership Check ---")
    test_members_updated = [103, 108, 110, 500]
    for member in test_members_updated:
        result = checker.check_membership(member)
        print(f"Is {member} a member? {result}")