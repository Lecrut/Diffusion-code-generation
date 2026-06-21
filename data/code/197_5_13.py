class ChecklistMembership:

    def __init__(self, allowed_items):
        self.allowed_frozenset = frozenset(allowed_items)

    @staticmethod
    def is_in_frozenset(element, frozenset_obj):
        return element in frozenset_obj
if __name__ == '__main__':
    checklist = ChecklistMembership([2, 4, 6, 8, 10])
    print(ChecklistMembership.is_in_frozenset(3, checklist.allowed_frozenset))
    print(ChecklistMembership.is_in_frozenset(6, checklist.allowed_frozenset))