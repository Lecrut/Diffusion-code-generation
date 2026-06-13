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
    initial_members = [101, 102, 103, 104, 105, 106, 107, 108]
    for member in initial_members:
        checker.add_member(member)
    print("--- Initial Membership Check ---")
    test_members = [101, 103, 109]
    for member in test_members:
        result = checker.check_membership(member)
        print(f"Is {member} a member? {result}")
    print("\n--- Performance Test with Large Set ---")
    large_set_size = 100000
    large_members = set(range(1, large_set_size + 1))
    checker.memberships = large_members
    start_time = time.perf_counter()
    num_checks = 10000
    test_ids = [i % large_set_size for i in range(num_checks)]
    for member_id in test_ids:
        checker.check_membership(member_id)
    end_time = time.perf_counter()
    print(f"Checked {num_checks} random IDs.")
    print(f"Time taken: {(end_time - start_time) * 1000:.3f} ms")