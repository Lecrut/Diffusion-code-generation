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
    sample_members = [101, 102, 103, 104, 105, 106, 107, 108]
    for member in sample_members:
        checker.add_member(member)
    print("--- Membership Checking System ---")
    test_members = [101, 103, 105, 999]
    for member in test_members:
        is_member = checker.check_membership(member)
        print(f"Checking membership for ID {member}: {'Member' if is_member else 'Not Member'}")
    print("\n--- Performance Test (Large Scale Simulation) ---")
    large_set_size = 100000
    large_memberships = set(range(1, large_set_size + 1))
    checker_large = MembershipChecker()
    checker_large.memberships = large_memberships
    start_time = time.perf_counter()
    checks_to_perform = list(large_memberships)
    for member in checks_to_perform:
        checker_large.check_membership(member)
    end_time = time.perf_counter()
    print(f"System initialized with {len(large_memberships)} members.")
    print(f"Time taken to perform {len(large_memberships)} checks: {(end_time - start_time) * 1000:.3f} ms")