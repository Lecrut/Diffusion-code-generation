class MembershipChecker:
    def __init__(self, members):
        self.members = set(members)

    def is_member(self, individual):
        return individual in self.members

if __name__ == '__main__':
    checker = MembershipChecker(["Alice", "Bob", "Charlie"])
    print(f"Is Alice a member? {checker.is_member('Alice')}")
    print(f"Is Bob a member? {checker.is_member('Bob')}")
    print(f"Is Eve a member? {checker.is_member('Eve')}")