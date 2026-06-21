class MembershipChecker:
    def __init__(self, items):
        self.items = set(items)

    def is_member(self, item):
        return item in self.items

if __name__ == '__main__':
    checker = MembershipChecker(["Alice", "Bob", "Charlie"])
    print(f"Alice is a member: {checker.is_member('Alice')}")
    print(f"Bob is a member: {checker.is_member('Bob')}")
    print(f"Zoe is a member: {checker.is_member('Zoe')}")