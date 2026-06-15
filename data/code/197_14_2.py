import time
class MembershipChecker:
    def __init__(self):
        self.memberships = set()
    def add_member(self, member_id):
        self.memberships.add(member_id)
    def check_membership(self, member_id):
        return member_id in self.memberships
if __name__ == '__main__':
    checker = MembershipChecker()
    initial_members = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    for member in initial_members:
        checker.add_member(member)
    print("--- Initial Setup ---")
    print(f"Total members loaded: {len(checker.memberships)}")
    checks = [101, 105, 111, 102, 99]
    print("\n--- Membership Checks ---")
    for member in checks:
        result = checker.check_membership(member)
        print(f"Checking membership for {member}: {result}")
    print("\n--- Performance Test (Large Scale) ---")
    large_set_size = 100000
    large_members = set(range(1, large_set_size + 1))
    checker.memberships = large_members
    test_checks = [i for i in range(1, large_set_size + 1)]
    start_time = time.perf_counter()
    for member in test_checks:
        checker.check_membership(member)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Testing membership check for {large_set_size} members took: {duration:.6f} seconds")