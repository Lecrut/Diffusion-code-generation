class MembershipChecker:
    def __init__(self):
        self.memberships = {}
    def add_membership(self, entity, group):
        if entity not in self.memberships:
            self.memberships[entity] = set()
        self.memberships[entity].add(group)
    def check_membership(self, entity, group):
        if entity in self.memberships:
            return group in self.memberships[entity]
        return False
if __name__ == '__main__':
    checker = MembershipChecker()
    checker.add_membership("Alice", "Admins")
    checker.add_membership("Alice", "Users")
    checker.add_membership("Bob", "Users")
    checker.add_membership("Charlie", "Admins")
    print(f"Is Alice a member of Admins? {checker.check_membership('Alice', 'Admins')}")
    print(f"Is Alice a member of Users? {checker.check_membership('Alice', 'Users')}")
    print(f"Is Bob a member of Admins? {checker.check_membership('Bob', 'Admins')}")
    print(f"Is David a member of Users? {checker.check_membership('David', 'Users')}")