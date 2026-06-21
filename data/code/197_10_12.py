class ChecklistMembershipChecker:
    def __init__(self, items):
        if not all(isinstance(item, str) for item in items):
            raise ValueError("All items must be strings")
        self.items_set = set(items)

    def is_member(self, item):
        return item in self.items_set

if __name__ == '__main__':
    checklist_items = ["Apple", "Banana", "Cherry"]
    checker = ChecklistMembershipChecker(checklist_items)
    print(f"Is 'Banana' a member? {checker.is_member('Banana')}")
    print(f"Is 'Grape' a member? {checker.is_member('Grape')}")