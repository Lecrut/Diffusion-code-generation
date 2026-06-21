class ChecklistMembershipChecker:

    def __init__(self, items):
        self.membership_set = set(items)

    def is_member(self, item):
        return item in self.membership_set
if __name__ == '__main__':
    items = ['Alice', 'Bob', 'Charlie']
    checker = ChecklistMembershipChecker(items)
    print(checker.is_member('Bob'))
    print(checker.is_member('Zoe'))