class MembershipChecker:
    def __init__(self):
        self.memberships = {}
    def add_membership(self, entity, group):
        if entity not in self.memberships:
            self.memberships[entity] = set()
        self.memberships[entity].add(group)
    def check_membership(self, entity, group):
        if entity in self.memberships and group in self.memberships[entity]:
            return True
        return False
if __name__ == '__main__':
    checker = MembershipChecker()
    checker.add_membership("Alice", "Admins")
    checker.add_membership("Alice", "Users")
    checker.add_membership("Bob", "Users")
    checker.add_membership("Charlie", "Admins")
    print(f"Alice is in Admins: {checker.check_membership('Alice', 'Admins')}")
    print(f"Alice is in Users: {checker.check_membership('Alice', 'Users')}")
    print(f"Bob is in Admins: {checker.check_membership('Bob', 'Admins')}")
    print(f"Charlie is in Admins: {checker.check_membership('Charlie', 'Admins')}")
    print(f"Bob is in Users: {checker.check_membership('Bob', 'Users')}")
    print(f"Alice is in Groups (Non-existent): {checker.check_membership('Alice', 'Guests')}")