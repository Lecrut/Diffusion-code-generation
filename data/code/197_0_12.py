class ChecklistManager:
    def __init__(self):
        self.membership_set = set()

    def add_item(self, item):
        self.membership_set.add(item)

    def remove_item(self, item):
        if item in self.membership_set:
            self.membership_set.remove(item)

    def check_membership(self, item):
        return item in self.membership_set

if __name__ == '__main__':
    checklist = ChecklistManager()
    checklist.add_item('task1')
    checklist.add_item('task2')
    print(f"Is 'task1' in the checklist? {checklist.check_membership('task1')}")
    print(f"Is 'task3' in the checklist? {checklist.check_membership('task3')}")
    checklist.remove_item('task1')
    print(f"Is 'task1' in the checklist after removal? {checklist.check_membership('task1')}")