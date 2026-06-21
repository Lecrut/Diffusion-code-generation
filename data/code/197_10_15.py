class MembershipChecker:
    def __init__(self, items):
        self.items_set = set(items)

    def is_member(self, item):
        return item in self.items_set

if __name__ == '__main__':
    checklist = ["apple", "banana", "cherry"]
    checker = MembershipChecker(checklist)
    print(f"Is 'banana' a member? {checker.is_member('banana')}")
    print(f"Is 'grape' a member? {checker.is_member('grape')}")