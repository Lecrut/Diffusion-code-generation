class ChecklistMembershipChecker:

    def __init__(self, items):
        if not all((isinstance(item, str) for item in items)):
            raise ValueError('All items must be strings')
        self.membership_set = set(items)

    def is_member(self, item):
        return item in self.membership_set
if __name__ == '__main__':
    checker = ChecklistMembershipChecker(['Alice', 'Bob', 'Charlie'])
    print(checker.is_member('Bob'))
    print(checker.is_member('Zoe'))