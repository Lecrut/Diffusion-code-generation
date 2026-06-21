class ChecklistMembershipChecker:
    def __init__(self, items):
        self.items_set = set(items)

    def is_member(self, item):
        return item in self.items_set

if __name__ == '__main__':
    checklist = ["Apple", "Banana", "Cherry"]
    checker = ChecklistMembershipChecker(checklist)
    print(f"Is 'Banana' a member? {checker.is_member('Banana')}")
    print(f"Is 'Grape' a member? {checker.is_member('Grape')}")