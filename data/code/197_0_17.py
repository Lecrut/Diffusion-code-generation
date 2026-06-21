class ChecklistManager:

    def __init__(self):
        self.membership = set()

    def add_member(self, item):
        self.membership.add(item)

    def remove_member(self, item):
        if item in self.membership:
            self.membership.remove(item)

    def check_membership(self, item):
        return item in self.membership
if __name__ == '__main__':
    checklist = ChecklistManager()
    checklist.add_member('apple')
    checklist.add_member('banana')
    print(checklist.check_membership('apple'))
    print(checklist.check_membership('orange'))
    checklist.remove_member('apple')
    print(checklist.check_membership('apple'))