class ChecklistMembershipChecker:

    def __init__(self, items):
        self.items = set(items)

    def is_member(self, item):
        return item in self.items
if __name__ == '__main__':
    checklist = ChecklistMembershipChecker(['Apple', 'Banana', 'Cherry'])
    print(checklist.is_member('Banana'))
    print(checklist.is_member('Grape'))