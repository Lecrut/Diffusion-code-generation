class ChecklistManager:

    def __init__(self):
        self.membership_set = set()

    def add_item(self, item):
        if not isinstance(item, (int, str)):
            raise ValueError('Item must be an integer or string')
        self.membership_set.add(item)

    def remove_item(self, item):
        if item in self.membership_set:
            self.membership_set.remove(item)
        else:
            raise KeyError(f'Item {item} not found in checklist')

    def check_membership(self, item):
        return item in self.membership_set
if __name__ == '__main__':
    manager = ChecklistManager()
    manager.add_item(10)
    manager.add_item('apple')
    print(manager.check_membership(10))
    print(manager.check_membership('apple'))
    manager.remove_item(10)
    print(manager.check_membership(10))