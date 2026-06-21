class ChecklistManager:
    def __init__(self):
        self.membership_set = set()

    def add_item(self, item):
        self.membership_set.add(item)

    def remove_item(self, item):
        if item in self.membership_set:
            self.membership_set.remove(item)

    def check_membership(self, target):
        return target in self.membership_set

if __name__ == '__main__':
    checklist = ChecklistManager()
    checklist.add_item('apple')
    checklist.add_item('banana')
    print(f"Is 'apple' in the checklist? {checklist.check_membership('apple')}")
    print(f"Is 'orange' in the checklist? {checklist.check_membership('orange')}")
    checklist.remove_item('apple')
    print(f"Is 'apple' in the checklist after removal? {checklist.check_membership('apple')}")