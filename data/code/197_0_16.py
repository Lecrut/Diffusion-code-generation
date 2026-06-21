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
    manager = ChecklistManager()
    manager.add_item('task1')
    manager.add_item('task2')
    print(f"Is 'task1' in the checklist? {manager.check_membership('task1')}")
    manager.remove_item('task1')
    print(f"Is 'task1' in the checklist after removal? {manager.check_membership('task1')}")