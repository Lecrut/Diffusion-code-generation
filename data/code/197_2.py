class MembershipChecker:
    def __init__(self):
        self._members = set()
    def add_member(self, member):
        self._members.add(member)
    def is_member(self, item):
        return item in self._members
if __name__ == '__main__':
    checker = MembershipChecker()
    checker.add_member("Alice")
    checker.add_member("Bob")
    checker.add_member("Charlie")
    print(f"Is Alice a member? {checker.is_member('Alice')}")
    print(f"Is Bob a member? {checker.is_member('Bob')}")
    print(f"Is David a member? {checker.is_member('David')}")