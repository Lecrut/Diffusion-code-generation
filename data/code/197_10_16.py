class ChecklistMembershipChecker:
    def __init__(self, items):
        self.items = set(items)

    def is_member(self, item):
        return item in self.items

if __name__ == '__main__':
    membership_data = ["Alice", "Bob", "Charlie"]
    checker = ChecklistMembershipChecker(membership_data)
    print(f"Alice is a member: {checker.is_member('Alice')}")
    print(f"Zoe is a member: {checker.is_member('Zoe')}")