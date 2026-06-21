class ChecklistManager:

    def __init__(self):
        self.membership = set()

    def add_item(self, item):
        self.membership.add(item)

    def remove_item(self, item):
        if item in self.membership:
            self.membership.remove(item)

    def check_membership(self, item):
        return item in self.membership
if __name__ == '__main__':
    checklist = ChecklistManager()
    checklist.add_item('Task 1')
    checklist.add_item('Task 2')
    print(checklist.check_membership('Task 1'))
    print(checklist.check_membership('Task 3'))
    checklist.remove_item('Task 1')
    print(checklist.check_membership('Task 1'))