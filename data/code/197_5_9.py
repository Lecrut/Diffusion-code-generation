class Checklist:

    def __init__(self, items):
        self.frozenset_items = frozenset(items)

    def is_member(self, item):
        return item in self.frozenset_items
if __name__ == '__main__':
    sample_checklist = Checklist([1, 2, 3, 4, 5])
    print(sample_checklist.is_member(3))
    print(sample_checklist.is_member(6))