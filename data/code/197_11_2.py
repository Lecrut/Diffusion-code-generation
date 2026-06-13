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
    checker.add_membership("Alice", "Developers")
    checker.add_membership("Bob", "Developers")
    checker.add_membership("Charlie", "Admins")
    print(f"Is Alice in Admins? {checker.check_membership('Alice', 'Admins')}")
    print(f"Is Alice in Developers? {checker.check_membership('Alice', 'Developers')}")
    print(f"Is Bob in Admins? {checker.check_membership('Bob', 'Admins')}")
    print(f"Is David in Developers? {checker.check_membership('David', 'Developers')}")