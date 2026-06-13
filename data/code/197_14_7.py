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
    print(f"Initial memberships loaded: {sorted(list(checker.memberships))}")
    check1 = 103
    result1 = checker.check_membership(check1)
    print(f"Checking membership for {check1}: {result1}")
    check2 = 999
    result2 = checker.check_membership(check2)
    print(f"Checking membership for {check2}: {result2}")
    checker.add_member(108)
    print(f"After adding member 108, current memberships: {sorted(list(checker.memberships))}")
    check3 = 108
    result3 = checker.check_membership(check3)
    print(f"Checking membership for {check3}: {result3}")