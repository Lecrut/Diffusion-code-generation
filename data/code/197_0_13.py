class ChecklistManager:

    def __init__(self, items=None):
        if not isinstance(items, (list, tuple, set)):
            raise ValueError('Items must be a list, tuple, or set')
        self.items = set(items)

    def add_item(self, item):
        if not isinstance(item, (int, str)):
            raise ValueError('Item must be an integer or string')
        self.items.add(item)

    def remove_item(self, item):
        if not isinstance(item, (int, str)):
            raise ValueError('Item must be an integer or string')
        if item in self.items:
            self.items.remove(item)
        else:
            raise KeyError(f'Item {item} not found in checklist')

    def check_membership(self, item):
        if not isinstance(item, (int, str)):
            raise ValueError('Item must be an integer or string')
        return item in self.items
if __name__ == '__main__':
    checklist = ChecklistManager([10, 20, 30])
    print(checklist.check_membership(20))
    checklist.add_item(40)
    print(checklist.check_membership(40))
    checklist.remove_item(20)
    print(checklist.check_membership(20))
    try:
        checklist.add_item('apple')
    except ValueError as e:
        print(e)
    try:
        checklist.check_membership(None)
    except ValueError as e:
        print(e)